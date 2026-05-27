# How-to: Test Hints With pytest

Use direct validator classes in unit tests for quick feedback.

## 1. Create a validator test

```python
from assertions_mate import Cql2Query
from assertions_mate.cql2_validator import Cql2Validator

def test_rule_fails_when_count_not_positive():
    validator = Cql2Validator(
        queries=[Cql2Query(id="q", cql2="count > 0", message="count must be positive")]
    )
    result = validator.validate_inputs({"count": 0})
    assert result is not None
```

## 2. Run the test

```bash
hatch run test:test-q examples/pytest-validation/test_validators_example.py
```

## Ready-to-run example in this repository

- `examples/pytest-validation/test_validators_example.py`
