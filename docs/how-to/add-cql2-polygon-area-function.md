# How-to: Add `polygon_area(...)` to the CQL2 Evaluator

This guide shows how to extend `assertions-mate` so CQL2 rules can compare polygon area against a fixed threshold.

## Goal

Enable expressions like:

```text
polygon_area(aoi) < 1000
```

## 1. Define the new function in a CQL2 hint

In your workflow hints, plug the suggested implementation:

```yaml
hints:
  - class: eoap:Cql2FilterHint
    custom_functions: |
        from shapely import geometry
        from typing import Any, List, Mapping, Union

        def polygon_area(input: Union[Mapping[str, Any], List[Any]]):
            """Return area for a GeoJSON Polygon payload or raw coordinates list."""
            if isinstance(input, dict):
                geo_type = input.get("type")
                coords = input.get("coordinates")
                if geo_type != "Polygon" or not coords:
                    raise ValueError("Input must be a GeoJSON Polygon with coordinates")
                geom = geometry.Polygon(coords[0])
                return geom.area

            if isinstance(input, list):
                geom = geometry.Polygon(input[0] if input and isinstance(input[0], list) else input)
                return geom.area

            raise ValueError(f"Unsupported polygon input type: {type(input)}")
    queries:
      - id: aoi-area-limit
        cql2: "polygon_area(aoi) < 1000"
        message: "AOI area must be smaller than 1000"
```

## 2. Validate with CLI

```bash
assertions-mate path/to/workflow.cwl --inputs path/to/inputs.yaml
```

## Notes on units

If AOI coordinates are lon/lat (EPSG:4326), `polygon_area` from Shapely returns degree-squared values, not square meters.

For metric thresholds, either:
- reproject geometry before computing area
- or compute geodesic area with a dedicated geodesic approach
