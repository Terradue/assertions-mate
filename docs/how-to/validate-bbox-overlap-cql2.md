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
    custom_functions: |
      from shapely import geometry
      from typing import Any, List, Mapping, Union

      def ensure_bbox(input: Union[Mapping[str, Any], List[float], str]):
          value = []

          if isinstance(input, dict):
              value = input["bbox"]
              if not value:
                  raise ValueError(f"Input {input} doesn't have a 'bbox' property")
          elif isinstance(input, str):
              value = [float(x) for x in str(input).split(",")]
          else:
              value = input

          return geometry.box(*value)
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
