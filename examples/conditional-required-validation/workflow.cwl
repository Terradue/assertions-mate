cwlVersion: v1.2
class: Workflow
id: conditional-required-validation
inputs:
  execution-mode:
    type: string
  aoi:
    type:
      - https://raw.githubusercontent.com/eoap/schemas/main/geojson.yaml#Polygon
      - "null"
outputs: {}
steps: {}
hints:
  - class: eoap:RegoPolicyHint
    module: |
      package workflow

      deny[msg] {
        input["execution-mode"] == "spatial"
        input["aoi"] == null
        msg := "aoi is required when execution-mode is spatial"
      }
    queries:
      - data.workflow.deny[_]
