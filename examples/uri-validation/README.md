# URI Validation Example (Rego + Packed CWL)

This example validates a URI input named `stack-uri` using CWL and a `RegoPolicyHint`.

## Files

- `workflow.cwl`: workflow with `stack-uri` and Rego checks.
- `inputs-valid.yaml`: valid URI input.
- `inputs-invalid.yaml`: invalid URI-like value.
- `inputs-null.yaml`: null input (expected to fail required Rego rule).

## Run

From repository root:

```bash
assertions-mate examples/uri-validation/workflow.cwl --inputs examples/uri-validation/inputs-valid.yaml
```

Try invalid:

```bash
assertions-mate examples/uri-validation/workflow.cwl --inputs examples/uri-validation/inputs-invalid.yaml
```

Try null:

```bash
assertions-mate examples/uri-validation/workflow.cwl --inputs examples/uri-validation/inputs-null.yaml
```
