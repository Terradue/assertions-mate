# Runtime Compatibility Reference

This page captures runtime-specific behavior observed in `assertions-mate` integrations.

## Rego Compatibility

- Recommended rule style: classic Rego

```rego
deny[msg] {
  condition
  msg := "human readable message"
}
```

- Query style used by examples:

```text
data.workflow.deny[_]
```

- Known incompatibility in some runtimes:

```rego
deny contains "..." if { ... }
```

This newer style can raise `Invalid literal` parser errors depending on `regopy` runtime behavior.

## CQL2 Compatibility

- Text and JSON CQL2 encodings are supported.
- Spatial predicates over GeoJSON payloads should use `ensure_spatial(...)` coercion:
  - `s_within(ensure_spatial(point), ensure_spatial(aoi))`
  - `s_intersects(ensure_spatial(a), ensure_spatial(b))`
- BBOX predicates should use `ensure_bbox(...)`:
  - `s_intersects(ensure_bbox(b1), ensure_bbox(b2))`

## CQL2 JSON From YAML

YAML scalar wrapper types can break evaluation unless normalized to builtin Python values.
The validator includes normalization before `parse_cql2_json`, which makes JSON-encoded rules reliable in current examples.

## External CWL Type References

Types such as:

- `https://raw.githubusercontent.com/eoap/schemas/main/string_format.yaml#DateTime`
- `https://raw.githubusercontent.com/eoap/schemas/main/geojson.yaml#Polygon`

may require online schema resolution and parser compatibility.

Testing guidance:
- Unit tests: prefer local scalar types for deterministic behavior.
- Integration tests: allow external refs and skip when offline.
