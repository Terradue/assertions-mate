# Datetime Validation Example (Rego)

This example validates a datetime input named `sensing-time` using `RegoPolicyHint`.

## Files

- `workflow.cwl`: workflow with classic Rego rules.
- `inputs-valid.yaml`: valid UTC datetime format.
- `inputs-invalid.yaml`: invalid datetime format.
- `inputs-null.yaml`: null input (expected to fail required check).

## Run

From repository root:

```bash
assertions-mate examples/datetime-validation/workflow.cwl --inputs examples/datetime-validation/inputs-valid.yaml
```

Try invalid:

```bash
assertions-mate examples/datetime-validation/workflow.cwl --inputs examples/datetime-validation/inputs-invalid.yaml
```

Try null:

```bash
assertions-mate examples/datetime-validation/workflow.cwl --inputs examples/datetime-validation/inputs-null.yaml
```
