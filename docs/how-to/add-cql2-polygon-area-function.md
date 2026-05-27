# How-to: Add `polygon_area(...)` to the CQL2 Evaluator

This guide shows how to extend `assertions-mate` so CQL2 rules can compare polygon area against a fixed threshold.

## Goal

Enable expressions like:

```text
polygon_area(aoi) < 1000
```

## 1. Update the evaluator function map

Edit [src/assertions_mate/cql2_validator.py](/data/work/github-terradue/assertions-mate/src/assertions_mate/cql2_validator.py) and:

1. add a helper function `polygon_area(...)`
2. register it in `NativeEvaluator(function_map=...)`

Suggested implementation:

```python
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


# inside Cql2Validator.__init__
self.evaluator = NativeEvaluator(
    function_map={
        "ensure_bbox": ensure_bbox,
        "polygon_area": polygon_area,
    },
    use_getattr=False,
)
```

## 2. Use the new function in a CQL2 hint

In your workflow hints:

```yaml
hints:
  - class: eoap:Cql2FilterHint
    queries:
      - id: aoi-area-limit
        cql2: "polygon_area(aoi) < 1000"
        message: "AOI area must be smaller than 1000"
```

## 3. Validate with CLI

```bash
assertions-mate path/to/workflow.cwl --inputs path/to/inputs.yaml
```

## Notes on units

If AOI coordinates are lon/lat (EPSG:4326), `polygon_area` from Shapely returns degree-squared values, not square meters.

For metric thresholds, either:
- reproject geometry before computing area
- or compute geodesic area with a dedicated geodesic approach
