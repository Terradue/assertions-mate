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

from assertions_mate.jsonschema_validator import JSONSchemaValidator


def test_validate_inputs_returns_none_for_valid_payload():
    validator = JSONSchemaValidator(
        schema={
            "type": "object",
            "properties": {"count": {"type": "integer"}},
            "required": ["count"],
        }
    )

    result = validator.validate_inputs({"count": 3})

    assert result is None


def test_validate_inputs_returns_problem_details_for_invalid_payload():
    validator = JSONSchemaValidator(
        schema={
            "type": "object",
            "properties": {"count": {"type": "integer"}},
            "required": ["count"],
        }
    )

    result = validator.validate_inputs({})

    assert result is not None
    assert result.status == 400
    assert result.errors is not None
    assert len(result.errors) == 1
    assert "required property" in result.errors[0].detail
