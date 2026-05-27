# How-to: Validate Required Property (Rego)

## 1. Define the typed input

```yaml
inputs:
  aoi:
    type: https://raw.githubusercontent.com/eoap/schemas/main/geojson.yaml#Polygon
```

## 2. Add Rego check

Require `aoi.properties.name`:

```yaml
hints:
  - class: eoap:RegoPolicyHint
    module: |
      package workflow

      deny[msg] {
        input["aoi"]["properties"]["name"] == null
        msg := "aoi.properties.name must be provided"
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

- `examples/required-property-validation/workflow.cwl`
- `examples/required-property-validation/inputs-valid.yaml`
- `examples/required-property-validation/inputs-invalid.yaml`
