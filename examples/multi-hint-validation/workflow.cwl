cwlVersion: v1.2
class: Workflow
id: multi-hint-validation
inputs:
  count:
    type: int
  aoi:
    type: https://raw.githubusercontent.com/eoap/schemas/main/geojson.yaml#Polygon
  candidate:
    type: https://raw.githubusercontent.com/eoap/schemas/main/geojson.yaml#Polygon
outputs: {}
steps: {}
hints:
  - class: eoap:JSONSchemaHint
    json_schema:
      type: object
      required: [count, aoi, candidate]
      properties:
        count:
          type: integer
          minimum: 1
  - class: eoap:RegoPolicyHint
    module: |
      package workflow

      deny[msg] {
        input["count"] > 10
        msg := "count must be <= 10"
      }
    queries:
      - data.workflow.deny[_]
  - class: eoap:Cql2FilterHint
    queries:
      - id: polygons-intersect
        cql2: "s_intersects(ensure_spatial(candidate), ensure_spatial(aoi))"
        message: "candidate must intersect aoi"
