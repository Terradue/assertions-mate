from assertions_mate import Cql2Query
from assertions_mate.cql2_validator import Cql2Validator, ensure_bbox


def test_ensure_bbox_accepts_list_and_string():
    bbox_from_list = ensure_bbox([0.0, 0.0, 1.0, 1.0])
    bbox_from_string = ensure_bbox("0,0,1,1")

    assert bbox_from_list.bounds == (0.0, 0.0, 1.0, 1.0)
    assert bbox_from_string.bounds == (0.0, 0.0, 1.0, 1.0)


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
