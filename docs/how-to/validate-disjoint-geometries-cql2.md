# How-to: Validate Geometries Are Disjoint (CQL2)

Assert two geometries do not overlap/intersect.

## 1. Define typed inputs

```yaml
inputs:
  g1:
    type: https://raw.githubusercontent.com/eoap/schemas/main/geojson.yaml#Polygon
  g2:
    type: https://raw.githubusercontent.com/eoap/schemas/main/geojson.yaml#Polygon
```

## 2. Add CQL2 check

```yaml
hints:
  - class: eoap:Cql2FilterHint
    queries:
      - id: geometries-disjoint
        cql2: "s_disjoint(ensure_spatial(g1), ensure_spatial(g2))"
        message: "g1 and g2 must be disjoint"
```

## 3. Validate with sample values

Run:

```bash
assertions-mate workflow.cwl --inputs inputs-valid.yaml
```

## Ready-to-run example in this repository

- `examples/disjoint-geometries-validation/workflow.cwl`
- `examples/disjoint-geometries-validation/inputs-valid.yaml`
- `examples/disjoint-geometries-validation/inputs-invalid.yaml`
