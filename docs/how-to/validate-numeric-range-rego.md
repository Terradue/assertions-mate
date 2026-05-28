# How-to: Validate Numeric Range (Rego)

## 1. Define the input

Require `count` in range `[1, 10]`.

```yaml
inputs:
  count:
    type: int
```

## 2. Add Rego checks

```yaml
hints:
  - class: eoap:RegoPolicyHint
    module: |
      package workflow

      deny[msg] {
        c := input["count"]
        c < 1
        msg := "count must be >= 1"
      }

      deny[msg] {
        c := input["count"]
        c > 10
        msg := "count must be <= 10"
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

- `examples/numeric-range-validation/workflow.cwl`
- `examples/numeric-range-validation/inputs-valid.yaml`
- `examples/numeric-range-validation/inputs-invalid.yaml`
