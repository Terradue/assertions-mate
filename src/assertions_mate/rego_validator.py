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
    RegoPolicyHint
)
from .error_models import (
    BusinessRuleViolation,
    ErrorDetail,
    ProblemDetails
)
from regopy import Interpreter
from typing import (
    Any,
    List,
    Mapping
)

class RegoValidator(BaseValidator):

    def __init__(
        self,
        module: str,
        queries: List[str]
    ):
        self.rego = Interpreter(True)
        self.rego.add_module("workflow", module)
        self.queries = queries

    def validate_inputs(
        self,
        data: Mapping[str, Any]
    ) -> ProblemDetails | None:
        errors_list = []

        self.rego.set_input(data)

        for query in self.queries:
            for result in self.rego.query(query):
                # result.expressions is a list of Expression objects
                exprs = result.expressions
                if not exprs:  # safety check
                    continue

                errors_list.append(
                    ErrorDetail(
                        pointer=query,
                        detail=exprs[0]
                    )
                )

        if errors_list:
            return BusinessRuleViolation(errors=errors_list)
