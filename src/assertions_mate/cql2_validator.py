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

from . import (
    BaseValidator,
    Cql2Query
)
from .error_models import (
    BusinessRuleViolation,
    ErrorDetail,
    ProblemDetails,
    ServerError
)
from pygeofilter.backends.native.evaluate import NativeEvaluator
from pygeofilter.parsers.cql2_text import parse as parse_cql2_text
from pygeofilter.parsers.cql2_json import parse as parse_cql2_json
from shapely import geometry
from typing import (
    Any,
    List,
    Mapping,
    Union
)

def ensure_bbox(input: Union[Mapping[str, Any], List[float], str]):
    value = []

    if isinstance(input, dict):
        value = input['bbox']
        if not value:
            raise ValueError(f"Input {input} doesn't have a 'bbox' property")
    elif isinstance(input, str):
        value = [float(x) for x in str(input).split(',')]
    else:
        value = input

    return geometry.box(*value)

class Cql2Validator(BaseValidator):

    def __init__(
        self,
        queries: List[Cql2Query]
    ):
        self.evaluator = NativeEvaluator(
            function_map={
                'ensure_bbox': ensure_bbox
            },
            use_getattr=False
        )

        self.queries = queries

    def validate_inputs(
        self,
        data: Mapping[str, Any]
    ) -> ProblemDetails | None:
        errors_list = []

        for filter in self.queries:
            ast = None

            if isinstance(filter.cql2, str):
                try:
                    ast = parse_cql2_text(filter.cql2)
                except Exception as e:
                    errors_list.append(
                        ErrorDetail(
                            pointer=filter.id,
                            detail=f"Filter does not look like a valid CQL2 Text encoded sentece: {e}"
                        )
                    )
            elif isinstance(filter.cql2, dict):
                try:
                    ast = parse_cql2_json(filter.cql2)
                except Exception as e:
                    errors_list.append(
                        ErrorDetail(
                            pointer=filter.id,
                            detail=f"Filter does not look like a valid CQL2 JSON encoded structure: {e}"
                        )
                    )
            else:
                errors_list.append(
                    ErrorDetail(
                        pointer=filter.id,
                        detail=f"Filter is expressed in an unrecognizible format: {type(filter.cql2)}"
                    )
                )

            if ast:
                predicate = self.evaluator.evaluate(ast)

                if not predicate(data):
                    errors_list.append(
                        ErrorDetail(
                            pointer=filter.id,
                            detail=filter.message
                        )
                    )

        if errors_list:
            return BusinessRuleViolation(errors=errors_list)

        return None
