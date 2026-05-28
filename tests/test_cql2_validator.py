from pathlib import Path

import yaml
from cwl_utils.parser import load_document_by_uri

from assertions_mate import Cql2FilterHint, Cql2Query, extract_assertion_hints
from assertions_mate.cql2_validator import Cql2Validator


def test_validate_inputs_reports_business_rule_violation_when_predicate_fails():
    validator = Cql2Validator(
        queries=[
            Cql2Query(
                id="rule-1",
                cql2="count > 5",
                message="Count must be greater than 5",
            )
        ]
    )

    result = validator.validate_inputs({"count": 2})

    assert result is not None
    assert result.status == 422
    assert result.errors is not None
    assert len(result.errors) == 1
    assert result.errors[0].pointer == "rule-1"
    assert result.errors[0].detail == "Count must be greater than 5"


def test_validate_inputs_reports_unrecognized_filter_format():
    validator = Cql2Validator(
        queries=[
            Cql2Query.model_construct(
                id="rule-2",
                cql2=5,
                message="should not be used",
            )
        ]
    )

    result = validator.validate_inputs({"count": 2})

    assert result is not None
    assert result.errors is not None
    assert len(result.errors) == 1
    assert result.errors[0].pointer == "rule-2"
    assert "unrecognizible format" in result.errors[0].detail


def test_validate_inputs_executes_ensure_bbox_custom_function_from_cwl_hint():
    example_dir = (
        Path(__file__).resolve().parents[1] / "examples" / "bbox-overlap-validation"
    )
    workflow = load_document_by_uri(
        path=example_dir / "workflow.cwl",
        load_all=True,
    )
    hints = [
        hint
        for hint in extract_assertion_hints(workflow)
        if isinstance(hint, Cql2FilterHint)
    ]

    assert len(hints) == 1
    assert hints[0].custom_functions is not None
    assert "ensure_bbox" in hints[0].custom_functions

    validator = hints[0].validator()

    with (example_dir / "inputs-valid.yaml").open(encoding="utf-8") as input_stream:
        valid_inputs = yaml.safe_load(input_stream)

    with (example_dir / "inputs-invalid.yaml").open(encoding="utf-8") as input_stream:
        invalid_inputs = yaml.safe_load(input_stream)

    assert validator.validate_inputs(valid_inputs) is None

    result = validator.validate_inputs(invalid_inputs)

    assert result is not None
    assert result.status == 422
    assert result.errors is not None
    assert len(result.errors) == 1
    assert result.errors[0].pointer == "bbox-overlap"
    assert result.errors[0].detail == "bbox_1 must overlap bbox_2"
