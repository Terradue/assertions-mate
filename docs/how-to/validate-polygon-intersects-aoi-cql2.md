# How-to: Validate Polygon Intersects AOI (CQL2)

Assert an input polygon intersects an AOI polygon.

## 1. Define typed inputs

```yaml
inputs:
  aoi:
    type: https://raw.githubusercontent.com/eoap/schemas/main/geojson.yaml#Polygon
  candidate:
    type: https://raw.githubusercontent.com/eoap/schemas/main/geojson.yaml#Polygon
```

## 2. Add CQL2 check

```yaml
hints:
  - class: eoap:Cql2FilterHint
    queries:
      - id: polygon-intersects
        cql2: "s_intersects(ensure_spatial(candidate), ensure_spatial(aoi))"
        message: "candidate must intersect aoi"
```

## 3. Validate with sample values

Run:

```bash
assertions-mate workflow.cwl --inputs inputs-valid.yaml
```

## Ready-to-run example in this repository

- `examples/polygon-intersects-validation/workflow.cwl`
- `examples/polygon-intersects-validation/inputs-valid.yaml`
- `examples/polygon-intersects-validation/inputs-invalid.yaml`
