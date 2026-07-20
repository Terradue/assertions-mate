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

from assertions_mate import Cql2Query
from assertions_mate.cql2_validator import Cql2Validator


def test_count_positive_rule_fails():
    validator = Cql2Validator(
        queries=[
            Cql2Query(
                id="count-positive",
                cql2="count > 0",
                message="count must be positive",
            )
        ]
    )

    result = validator.validate_inputs({"count": 0})

    assert result is not None
    assert result.errors is not None
    assert result.errors[0].pointer == "count-positive"
