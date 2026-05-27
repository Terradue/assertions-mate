# How-to: Author CQL2 Rules in JSON Encoding

You can provide `cql2` as JSON, not only text.

## 1. Define the input

```yaml
inputs:
  mode:
    type: string
```

## 2. Add CQL2 JSON rule

```yaml
hints:
  - class: eoap:Cql2FilterHint
    queries:
      - id: mode-is-strict
        cql2:
          op: "="
          args:
            - property: mode
            - "strict"
        message: "mode must be strict"
```

## 3. Validate with sample values

Valid:

```yaml
mode: "strict"
```

Run:

```bash
assertions-mate workflow.cwl --inputs inputs-valid.yaml
```

## Ready-to-run example in this repository

- `examples/cql2-json-validation/workflow.cwl`
- `examples/cql2-json-validation/inputs-valid.yaml`
- `examples/cql2-json-validation/inputs-invalid.yaml`
