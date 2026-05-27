cwlVersion: v1.2
class: Workflow
id: disjoint-geometries-validation
inputs:
  g1:
    type: https://raw.githubusercontent.com/eoap/schemas/main/geojson.yaml#Polygon
  g2:
    type: https://raw.githubusercontent.com/eoap/schemas/main/geojson.yaml#Polygon
outputs: {}
steps: {}
hints:
  - class: eoap:Cql2FilterHint
    queries:
      - id: geometries-disjoint
        cql2: "s_disjoint(ensure_spatial(g1), ensure_spatial(g2))"
        message: "g1 and g2 must be disjoint"
