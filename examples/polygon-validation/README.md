# Polygon Validation Example (CQL2 + Packed CWL)

This example follows a packed CWL style using `$graph` and `SchemaDefRequirement` imports (including `geojson.yaml`).

## Files

- `workflow.cwl`: packed CWL workflow with `eoap:Cql2FilterHint` checks over `aoi`.
- `inputs-valid.yaml`: valid Polygon payload.
- `inputs-invalid.yaml`: invalid payload (`aoi.type` is `Point`).

## Run

From repository root:

```bash
assertions-mate examples/polygon-validation/workflow.cwl --inputs examples/polygon-validation/inputs-valid.yaml
```

Try invalid input:

```bash
assertions-mate examples/polygon-validation/workflow.cwl --inputs examples/polygon-validation/inputs-invalid.yaml
```
