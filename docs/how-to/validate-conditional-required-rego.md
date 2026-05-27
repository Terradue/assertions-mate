# How-to: Validate Conditional Required Field (Rego)

Require `aoi` only for spatial execution mode.

## 1. Define the inputs

```yaml
inputs:
  execution-mode:
    type: string
  aoi:
    type:
      - https://raw.githubusercontent.com/eoap/schemas/main/geojson.yaml#Polygon
      - "null"
```

## 2. Add Rego check

```yaml
hints:
  - class: eoap:RegoPolicyHint
    module: |
      package workflow

      deny[msg] {
        input["execution-mode"] == "spatial"
        input["aoi"] == null
        msg := "aoi is required when execution-mode is spatial"
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

- `examples/conditional-required-validation/workflow.cwl`
- `examples/conditional-required-validation/inputs-valid.yaml`
- `examples/conditional-required-validation/inputs-invalid.yaml`
