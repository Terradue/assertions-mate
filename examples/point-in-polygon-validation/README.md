# Point in Polygon Validation Example (CQL2)

This example validates that `point` is inside `aoi` using `s_within(ensure_spatial(point), ensure_spatial(aoi))`.

## Files

- `workflow.cwl`
- `inputs-valid.yaml`
- `inputs-invalid.yaml`

## Run

From repository root:

```bash
assertions-mate examples/point-in-polygon-validation/workflow.cwl --inputs examples/point-in-polygon-validation/inputs-valid.yaml
```

Try invalid input:

```bash
assertions-mate examples/point-in-polygon-validation/workflow.cwl --inputs examples/point-in-polygon-validation/inputs-invalid.yaml
```
