cwlVersion: v1.2
class: Workflow
id: polygon-aoi
requirements:
  - class: SchemaDefRequirement
    types:
      - $import: https://raw.githubusercontent.com/eoap/schemas/main/string_format.yaml
      - $import: https://raw.githubusercontent.com/eoap/schemas/main/geojson.yaml
inputs:
  aoi:
    label: Area of interest
    doc: Area of interest
    type:
      - https://raw.githubusercontent.com/eoap/schemas/main/geojson.yaml#Polygon
      - "null"
outputs: {}
steps: {}
hints:
  - class: eoap:Cql2FilterHint
    queries:
      - id: aoi-present
        cql2: "aoi IS NOT NULL"
        message: "aoi must be provided"
      - id: aoi-type-is-polygon
        cql2: "aoi.type = 'Polygon'"
        message: "aoi.type must be Polygon"
      - id: aoi-bbox-present
        cql2: "aoi.bbox IS NOT NULL"
        message: "aoi.bbox must be provided"
