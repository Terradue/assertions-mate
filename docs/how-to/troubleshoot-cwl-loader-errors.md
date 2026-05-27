# How-to: Troubleshoot CWL Loader Errors

When validation fails before hints execute, the CWL document may be rejected by `cwl_utils`.

## Common symptom

- `schema_salad.exceptions.ValidationException`
- messages around invalid `requirements` field shape

## Checklist

1. Start with a minimal single-workflow document (`class: Workflow`, `cwlVersion: v1.2`).
2. Add one input at a time and re-run.
3. If failures appear after adding `requirements`, temporarily remove that section to isolate parser compatibility.
4. Keep examples runnable first; reintroduce advanced schema refs after parser behavior is confirmed.

## Tip

Different environments can parse the same CWL differently depending on exact `cwl_utils` and schema-salad versions.
