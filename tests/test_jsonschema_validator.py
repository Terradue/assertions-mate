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
