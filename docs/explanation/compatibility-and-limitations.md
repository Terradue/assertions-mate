# Compatibility and Limitations

This page explains where runtime behavior depends on parser and backend versions.

## Rego Runtime Coupling

Rego syntax support is runtime-dependent.

Stable pattern in current examples:

```rego
deny[msg] {
  condition
  msg := "..."
}
```

Depending on runtime, newer syntax forms can fail with parser errors such as `Invalid literal`.

## CQL2 Backend Constraints

CQL2 spatial predicates operate reliably when payloads are coerced with helper functions:

- `ensure_spatial(...)` for GeoJSON geometry objects
- `ensure_bbox(...)` for bbox data

Without coercion, backend exceptions can occur because predicates receive non-geometry objects.

## External CWL Type References

External schema refs (for example EOAP `#DateTime`, `#Polygon`) may require online resolution and parser compatibility.

Operational impact:
- local/offline environments may fail to resolve external refs
- integration tests should allow offline skip behavior

## JSON CQL2 From YAML

YAML-native scalar wrappers can affect CQL2 JSON evaluation if not normalized.

Current validator behavior includes normalization to builtin Python values before parsing CQL2 JSON, improving reliability.
