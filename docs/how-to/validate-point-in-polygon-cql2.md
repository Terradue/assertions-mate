# How-to: Validate Point in Polygon with CQL2

This guide shows how to assert that an input point is inside an AOI polygon using `eoap:Cql2FilterHint`.

## 1. Define typed inputs

Use EOAP GeoJSON schema types for both polygon and point.

```yaml
inputs:
  aoi:
    label: Area of interest
    doc: Area of interest
    type: https://raw.githubusercontent.com/eoap/schemas/main/geojson.yaml#Polygon

  point:
    label: Point of interest
    doc: Point to test against AOI
    type: https://raw.githubusercontent.com/eoap/schemas/main/geojson.yaml#Point
```

## 2. Add CQL2 rule

```yaml
hints:
  - class: eoap:Cql2FilterHint
    queries:
      - id: point-in-polygon
        cql2: "s_within(ensure_spatial(point), ensure_spatial(aoi))"
        message: "point must be inside aoi"
```

## 3. Validate with sample values

```bash
assertions-mate path/to/workflow.cwl --inputs path/to/inputs.yaml
```

## Ready-to-run example in this repository

- `examples/point-in-polygon-validation/workflow.cwl`
- `examples/point-in-polygon-validation/inputs-valid.yaml`
- `examples/point-in-polygon-validation/inputs-invalid.yaml`
