cwlVersion: v1.2
class: Workflow
id: required-property-validation
inputs:
  aoi:
    type: https://raw.githubusercontent.com/eoap/schemas/main/geojson.yaml#Polygon
outputs: {}
steps: {}
hints:
  - class: eoap:RegoPolicyHint
    module: |
      package workflow

      deny[msg] {
        input["aoi"]["properties"]["name"] == null
        msg := "aoi.properties.name must be provided"
      }
    queries:
      - data.workflow.deny[_]
