# How-to: Combine Multiple Hints in One Workflow

Use `JSONSchemaHint`, `RegoPolicyHint`, and `Cql2FilterHint` together to enforce structure, policy, and spatial predicates.

## 1. Define the inputs

```yaml
inputs:
  count:
    type: int
  aoi:
    type: https://raw.githubusercontent.com/eoap/schemas/main/geojson.yaml#Polygon
  candidate:
    type: https://raw.githubusercontent.com/eoap/schemas/main/geojson.yaml#Polygon
```

## 2. Add multiple hints

```yaml
hints:
  - class: eoap:JSONSchemaHint
    json_schema:
      type: object
      required: [count, aoi, candidate]
      properties:
        count:
          type: integer
          minimum: 1
  - class: eoap:RegoPolicyHint
    module: |
      package workflow
      deny[msg] {
        input["count"] > 10
        msg := "count must be <= 10"
      }
    queries:
      - data.workflow.deny[_]
  - class: eoap:Cql2FilterHint
    queries:
      - id: spatial-check
        cql2: "s_intersects(ensure_spatial(candidate), ensure_spatial(aoi))"
        message: "candidate must intersect aoi"
```

## 3. Validate with sample values

Run:

```bash
assertions-mate workflow.cwl --inputs inputs-valid.yaml
```

## Ready-to-run example in this repository

- `examples/multi-hint-validation/workflow.cwl`
- `examples/multi-hint-validation/inputs-valid.yaml`
- `examples/multi-hint-validation/inputs-invalid.yaml`
