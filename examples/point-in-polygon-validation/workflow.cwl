cwlVersion: v1.2
class: Workflow
id: point-in-polygon-validation
label: Point in Polygon Validation
doc: Validate that a point is inside an AOI polygon using CQL2.
inputs:
  aoi:
    label: Area of interest
    doc: Area of interest
    type: https://raw.githubusercontent.com/eoap/schemas/main/geojson.yaml#Polygon

  point:
    label: Point of interest
    doc: Point to test against AOI
    type: https://raw.githubusercontent.com/eoap/schemas/main/geojson.yaml#Point
outputs: {}
steps: {}
hints:
  - class: eoap:Cql2FilterHint
    queries:
      - id: point-in-polygon
        cql2: "s_within(ensure_spatial(point), ensure_spatial(aoi))"
        message: "point must be inside aoi"
