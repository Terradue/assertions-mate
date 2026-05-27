# How-to: Validate BBOX Overlap (CQL2)

## 1. Define the inputs

```yaml
inputs:
  bbox_1:
    type: string
  bbox_2:
    type: string
```

## 2. Add CQL2 check

```yaml
hints:
  - class: eoap:Cql2FilterHint
    queries:
      - id: bbox-overlap
        cql2: "s_intersects(ensure_bbox(bbox_1), ensure_bbox(bbox_2))"
        message: "bbox_1 must overlap bbox_2"
```

## 3. Validate with sample values

Run:

```bash
assertions-mate workflow.cwl --inputs inputs-valid.yaml
```

## Ready-to-run example in this repository

- `examples/bbox-overlap-validation/workflow.cwl`
- `examples/bbox-overlap-validation/inputs-valid.yaml`
- `examples/bbox-overlap-validation/inputs-invalid.yaml`
