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

from .error_models import ProblemDetails
from abc import (
    ABC,
    abstractmethod
)
from cwl2ogc import BaseCWLtypes2OGCConverter
from loguru import logger
from pydantic import (
    BaseModel,
    computed_field,
    model_serializer
)
from typing import (
    Any,
    List,
    Mapping,
    Optional
)

class BaseValidator(ABC):

    @abstractmethod
    def validate_inputs(
        self,
        data: Mapping[str, Any]
    ) -> ProblemDetails | None:
        pass

class AssertionHint(BaseModel):
    parent_workflow: Optional[Any] = None

    @property
    @computed_field
    @abstractmethod
    def annotation(self) -> str:
        pass

    @abstractmethod
    def validator(self) -> BaseValidator:
        pass

class JSONSchemaHint(AssertionHint):
    json_schema: Mapping[str, Any] = {}

    @staticmethod
    def get_annotation_name() -> str:
        return 'eoap.ogc.org/inputs-json-schema'

    @property
    def annotation(self) -> str:
        return JSONSchemaHint.get_annotation_name()

    @model_serializer
    def ser_model(self) -> Mapping[str, Any]:
        return BaseCWLtypes2OGCConverter(self.parent_workflow).get_inputs_json_schema() if self.parent_workflow is not None else self.json_schema
 
    def validator(self) -> BaseValidator:
        from .jsonschema_validator import JSONSchemaValidator
        schema = BaseCWLtypes2OGCConverter(self.parent_workflow).get_inputs_json_schema() if self.parent_workflow is not None else self.json_schema
        return JSONSchemaValidator(schema=schema)

class RegoPolicyHint(AssertionHint):

    @staticmethod
    def get_annotation_name() -> str:
        return 'eoap.ogc.org/inputs-rego-policy'

    module: str
    queries: List[str]

    @property
    def annotation(self) -> str:
        return RegoPolicyHint.get_annotation_name()

    @model_serializer
    def ser_model(self) -> Mapping[str, Any]:
        return {
            'queries': self.queries,
            'module': self.module
        }

    def validator(self) -> BaseValidator:
        from .rego_validator import RegoValidator
        return RegoValidator(
            queries=self.queries,
            module=self.module
        )

class Cql2Query(BaseModel):
    id: str
    cql2: str | Mapping[str, Any]
    message: str

class Cql2FilterHint(AssertionHint):

    @staticmethod
    def get_annotation_name() -> str:
        return 'eoap.ogc.org/inputs-cql2-filter'

    queries: List[Cql2Query]

    @property
    def annotation(self) -> str:
        return Cql2FilterHint.get_annotation_name()

    @model_serializer
    def ser_model(self) -> Mapping[str, Any]:
        return {
            'queries': self.queries
        }

    def validator(self) -> BaseValidator:
        from .cql2_validator import Cql2Validator
        return Cql2Validator(
            queries=self.queries
        )

def _get_assertion_hint_by_name(
    parent_workflow: Any,
    hint: Mapping[str, Any]
) -> AssertionHint | None:
    fqn_hint_kind = hint['class']

    logger.debug(f"Analysing hint: {fqn_hint_kind}")

    if 'eoap:' in fqn_hint_kind:
        hint_kind_name = fqn_hint_kind.split(':')[-1]

        logger.debug(f"Mapping {fqn_hint_kind} to {AssertionHint.__name__}:")

        try:
            hint_kind = globals()[hint_kind_name]
            return hint_kind(parent_workflow=parent_workflow, **hint)
        except Exception as e:
            logger.error(f"An error occurred while mapping {fqn_hint_kind} to {AssertionHint.__name__}: {e}")
            return None

    return None

def extract_assertion_hints(
    workflow: Any
) -> List[AssertionHint]:
    assertion_hints = []

    if workflow.hints:
        for hint in workflow.hints:
            if isinstance(hint, dict):
                hint_instance = _get_assertion_hint_by_name(parent_workflow=workflow, hint=hint)

                if hint_instance:
                    assertion_hints.append(hint_instance)
    else:
        logger.debug(f"No hints defined in current #{workflow.id.split('#')[-1]} {workflow.class_} ({workflow.cwlVersion})")

    return assertion_hints

