# Copyright 2025 Terradue
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
from json import JSONDecodeError
from pathlib import Path
from typing import Any, Mapping
from urllib.parse import urlparse

import requests
import yaml
from jsonschema import Draft202012Validator
from referencing import Registry as ReferencingRegistry
from referencing import Resource
from referencing.exceptions import NoSuchResource
from referencing.jsonschema import DRAFT202012
from session_adapters.file_adapter import FileAdapter
from session_adapters.oci_adapter import OCIAdapter
from session_adapters.s3_adapter import S3Adapter

from . import BaseValidator
from .error_models import ErrorDetail, InvalidBodyPropertyFormat, ProblemDetails


_REMOTE_SCHEMA_TIMEOUT_SECONDS = 10


class JSONSchemaRegistry:
    def __init__(
        self,
        timeout: int = _REMOTE_SCHEMA_TIMEOUT_SECONDS,
    ):
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "assertions-mate"})
        self.session.mount("file://", FileAdapter())
        self.session.mount("s3://", S3Adapter())
        self.session.mount("oci://", OCIAdapter())
        self.timeout = timeout

    @staticmethod
    def _schema_format_from_content_type(content_type: str | None) -> str | None:
        if not content_type:
            return None

        media_type = content_type.split(";", 1)[0].strip().lower()

        if media_type == "application/json" or media_type.endswith("+json"):
            return "json"

        if media_type in {
            "application/yaml",
            "application/x-yaml",
            "text/yaml",
            "text/x-yaml",
        } or media_type.endswith("+yaml"):
            return "yaml"

        return None

    @staticmethod
    def _schema_format_from_uri(uri: str) -> str | None:
        path = urlparse(uri).path.lower()

        if path.endswith(".json"):
            return "json"

        if path.endswith((".yaml", ".yml")):
            return "yaml"

        return None

    def _parse_schema(
        self,
        payload: bytes,
        uri: str,
        content_type: str | None = None,
    ) -> Any:
        text = payload.decode("utf-8")
        preferred_format = (
            self._schema_format_from_content_type(content_type)
            or self._schema_format_from_uri(uri)
            or "json"
        )
        formats = [preferred_format] + [
            candidate for candidate in ("json", "yaml") if candidate != preferred_format
        ]

        last_error: Exception | None = None
        for schema_format in formats:
            try:
                if schema_format == "json":
                    return json.loads(text)

                return yaml.safe_load(text)
            except (JSONDecodeError, yaml.YAMLError) as error:
                last_error = error

        raise ValueError(f"Unable to parse JSON Schema from {uri}") from last_error

    @staticmethod
    def _schema_request_uri(uri: str) -> str:
        parsed_uri = urlparse(uri)
        if parsed_uri.scheme:
            return uri

        path = Path(uri)
        if not path.exists():
            raise NoSuchResource(ref=uri)

        return path.absolute().as_uri()

    def load_schema(self, uri: str) -> Any:
        try:
            response = self.session.get(
                self._schema_request_uri(uri),
                timeout=self.timeout,
            )
        except requests.exceptions.InvalidSchema as error:
            raise NoSuchResource(ref=uri) from error

        if response.status_code == 404:
            raise NoSuchResource(ref=uri)

        response.raise_for_status()

        return self._parse_schema(
            payload=response.content,
            uri=uri,
            content_type=response.headers.get("Content-Type"),
        )

    def retrieve(self, uri: str) -> Resource[Any]:
        return DRAFT202012.create_resource(self.load_schema(uri))

    def as_referencing_registry(self) -> ReferencingRegistry[Any]:
        return ReferencingRegistry(retrieve=self.retrieve)


class JSONSchemaValidator(BaseValidator):
    def __init__(
        self,
        schema: Mapping[str, Any],
    ):
        self.validator = Draft202012Validator(
            schema,
            registry=JSONSchemaRegistry().as_referencing_registry(),
        )

    def validate_inputs(self, data: Mapping[str, Any]) -> ProblemDetails | None:
        errors_list = []

        for error in self.validator.iter_errors(data):
            print(error.__dict__)

            errors_list.append(
                ErrorDetail(
                    detail=error.message,
                    pointer=f"#/{'/'.join(error.path)}"
                    if error.path and isinstance(error.path, str)
                    else None,
                    code=".".join(error.schema_path),
                )
            )

        if errors_list:
            return InvalidBodyPropertyFormat(errors=errors_list)

        return None
