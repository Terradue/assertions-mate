# Error Reference

This page categorizes common errors and where they occur.

## 1. CWL Load/Parse Errors

Stage: before any validator is created.

Typical signature:
- `schema_salad.exceptions.ValidationException`

Common causes:
- CWL structure not accepted by current `cwl_utils` runtime
- parser/runtime mismatch for `requirements` or external refs

## 2. Hint Setup Errors

Stage: `Setting up validator for ...`

Typical signatures:
- Rego parser errors (`Invalid literal`)
- JSON schema setup errors

Effect:
- the failing hint validator is skipped
- remaining validators may still run

## 3. Validation Violations

Stage: validator execution.

Typical signatures:
- `... detected violations below:`
- one or more `[pointer] detail` entries

Examples:
- `[data.workflow.deny[_]] count must be <= 10`
- `[point-in-polygon] point must be inside aoi`

## 4. Runtime Exceptions During Validation

Stage: inside predicate evaluation.

Typical causes:
- invalid spatial coercion in CQL2 expression
- unsupported node/value type in evaluator backend

Mitigation:
- use `ensure_spatial(...)` for GeoJSON geometry payloads
- prefer validated example patterns from `docs/how-to/`
