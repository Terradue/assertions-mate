cwlVersion: v1.2
class: Workflow
id: bbox-overlap-validation
inputs:
  bbox_1:
    type: string
  bbox_2:
    type: string
outputs: {}
steps: {}
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
