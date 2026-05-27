cwlVersion: v1.2
class: Workflow
id: polygon-intersects-validation
inputs:
  aoi:
    type: https://raw.githubusercontent.com/eoap/schemas/main/geojson.yaml#Polygon
  candidate:
    type: https://raw.githubusercontent.com/eoap/schemas/main/geojson.yaml#Polygon
outputs: {}
steps: {}
hints:
  - class: eoap:Cql2FilterHint
    queries:
      - id: polygon-intersects
        cql2: "s_intersects(ensure_spatial(candidate), ensure_spatial(aoi))"
        message: "candidate must intersect aoi"
