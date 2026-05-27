# How-to: Check Polygon AOI Area with CQL2

This page answers a practical question: can `assertions-mate` validate that a polygon AOI area is smaller than a fixed value using CQL2?

## Short answer

Not with the current implementation as-is.

## Why it is not currently feasible

`assertions-mate` uses `pygeofilter` with this evaluator setup:

- only one custom function is registered: `ensure_bbox(...)`
- property access on function return values (such as `.area`) is not supported by the CQL2 parser used here
- no built-in `area(...)` function is registered

So expressions like these fail:

- `area(aoi) < 1000`
- `ensure_bbox(aoi).area < 1000`

## What would make it feasible

Add a custom numeric function to `Cql2Validator` (for example `polygon_area`) and call it directly in CQL2:

```text
polygon_area(aoi) < 1000
```

At implementation level, this means:

1. Add a Python helper that converts GeoJSON Polygon coordinates to a Shapely geometry and returns `.area`.
2. Register that helper in `NativeEvaluator(function_map=...)`.
3. Use that function in `eoap:Cql2FilterHint` queries.

## Important caveat about units

For lon/lat coordinates (e.g. EPSG:4326), Shapely area is in degree-squared, not square meters.
If you need metric area thresholds, reproject geometry before area calculation or use a geodesic area method.

## Current alternatives

- Use `eoap:RegoPolicyHint` and compute area in Rego only if your data model already provides area as a numeric input.
- Precompute AOI area upstream and validate the numeric field with CQL2 (`aoi_area < threshold`).
