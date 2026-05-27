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
