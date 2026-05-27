# How-to: Validate Cross-Field Dependency (Rego)

Require `threshold` when `mode` is `strict`.

## 1. Define the inputs

```yaml
inputs:
  mode:
    type: string
  threshold:
    type:
      - int
      - "null"
```

## 2. Add Rego check

```yaml
hints:
  - class: eoap:RegoPolicyHint
    module: |
      package workflow

      deny[msg] {
        input["mode"] == "strict"
        input["threshold"] == null
        msg := "threshold is required when mode is strict"
      }
    queries:
      - data.workflow.deny[_]
```

## 3. Validate with sample values

Run:

```bash
assertions-mate workflow.cwl --inputs inputs-valid.yaml
```

## Ready-to-run example in this repository

- `examples/cross-field-dependency-validation/workflow.cwl`
- `examples/cross-field-dependency-validation/inputs-valid.yaml`
- `examples/cross-field-dependency-validation/inputs-invalid.yaml`
