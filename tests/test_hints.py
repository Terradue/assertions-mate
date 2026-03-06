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
