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

from assertions_mate import Cql2FilterHint, JSONSchemaHint, extract_assertion_hints


class DummyWorkflow:
    def __init__(self, hints):
        self.id = "file:///tmp/workflow.cwl#main"
        self.class_ = "Workflow"
        self.cwlVersion = "v1.2"
        self.hints = hints


def test_extract_assertion_hints_maps_supported_hint_types():
    workflow = DummyWorkflow(
        hints=[
            {
                "class": "eoap:JSONSchemaHint",
                "json_schema": {"type": "object"},
            },
            {
                "class": "eoap:Cql2FilterHint",
                "queries": [
                    {
                        "id": "rule-1",
                        "cql2": "count > 0",
                        "message": "count must be positive",
                    }
                ],
            },
        ]
    )

    hints = extract_assertion_hints(workflow)

    assert len(hints) == 2
    assert isinstance(hints[0], JSONSchemaHint)
    assert isinstance(hints[1], Cql2FilterHint)


def test_extract_assertion_hints_ignores_unknown_or_non_mapping_hints():
    workflow = DummyWorkflow(
        hints=[
            {"class": "eoap:DoesNotExistHint"},
            "not-a-dict",
        ]
    )

    hints = extract_assertion_hints(workflow)

    assert hints == []
