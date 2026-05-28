# How-to: Validate Optional Input (Rego)

Validate an optional input only when present.

## 1. Define the input

```yaml
inputs:
  optional-code:
    type:
      - string
      - "null"
```

## 2. Add Rego check

```yaml
hints:
  - class: eoap:RegoPolicyHint
    module: |
      package workflow

      deny[msg] {
        v := input["optional-code"]
        v != null
        not regex.match("^[A-Z]{3}$", v)
        msg := "optional-code must be 3 uppercase letters"
      }
    queries:
      - data.workflow.deny[_]
```

## 3. Validate with sample values

Valid:

```yaml
optional-code: "ABC"
```

Run:

```bash
assertions-mate workflow.cwl --inputs inputs-valid.yaml
```

## Ready-to-run example in this repository

- `examples/optional-input-validation/workflow.cwl`
- `examples/optional-input-validation/inputs-valid.yaml`
- `examples/optional-input-validation/inputs-invalid.yaml`
