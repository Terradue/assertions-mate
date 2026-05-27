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
    queries:
      - id: bbox-overlap
        cql2: "s_intersects(ensure_bbox(bbox_1), ensure_bbox(bbox_2))"
        message: "bbox_1 must overlap bbox_2"
