from assertions_mate import (
    Cql2FilterHint,
    JSONSchemaHint,
    RegoPolicyHint,
    extract_assertion_hints,
)


class DummyWorkflow:
    def __init__(self, hints):
        self.id = "file:///tmp/workflow.cwl#main"
        self.class_ = "Workflow"
        self.cwlVersion = "v1.2"
        self.hints = hints


def test_extract_assertion_hints_maps_multi_hint_workflow_from_howto():
    workflow = DummyWorkflow(
        hints=[
            {
                "class": "eoap:JSONSchemaHint",
                "json_schema": {
                    "type": "object",
                    "required": ["count"],
                    "properties": {"count": {"type": "integer", "minimum": 1}},
                },
            },
            {
                "class": "eoap:RegoPolicyHint",
                "module": """
                package workflow

                deny[msg] {
                  input["count"] > 10
                  msg := "count must be <= 10"
                }
                """,
                "queries": ["data.workflow.deny[_]"],
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

    assert len(hints) == 3
    assert isinstance(hints[0], JSONSchemaHint)
    assert isinstance(hints[1], RegoPolicyHint)
    assert isinstance(hints[2], Cql2FilterHint)


def test_extract_assertion_hints_maps_uri_host_rego_hint_from_howto():
    workflow = DummyWorkflow(
        hints=[
            {
                "class": "eoap:RegoPolicyHint",
                "module": """
                package workflow

                deny[msg] {
                  uri := input["input-uri"]
                  not startswith(uri, "https://")
                  msg := "input-uri must start with https://"
                }
                """,
                "queries": ["data.workflow.deny[_]"],
            }
        ]
    )

    hints = extract_assertion_hints(workflow)

    assert len(hints) == 1
    assert isinstance(hints[0], RegoPolicyHint)
