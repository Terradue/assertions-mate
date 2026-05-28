# Date Range Validation Example (Rego)

This example validates that `end-date` is greater than `start-date`.

## Files

- `workflow.cwl`: workflow with Rego checks.
- `inputs-valid.yaml`: end-date is after start-date.
- `inputs-invalid.yaml`: end-date is before start-date.
- `inputs-null.yaml`: null start-date.

## Run

From repository root:

```bash
assertions-mate examples/date-range-validation/workflow.cwl --inputs examples/date-range-validation/inputs-valid.yaml
```

Try invalid ordering:

```bash
assertions-mate examples/date-range-validation/workflow.cwl --inputs examples/date-range-validation/inputs-invalid.yaml
```

Try null input:

```bash
assertions-mate examples/date-range-validation/workflow.cwl --inputs examples/date-range-validation/inputs-null.yaml
```
