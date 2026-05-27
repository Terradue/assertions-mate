cwlVersion: v1.2

class: Workflow
id: uri-validation
label: URI Input Validation
doc: Validate URI-like inputs for EOAP workflows.
requirements:
  - class: SchemaDefRequirement
    types:
      - $import: https://raw.githubusercontent.com/eoap/schemas/main/string_format.yaml
inputs:
  stack-uri:
    id: stack-uri
    label: "Snapping Stack URI"
    doc: "SNAPPING Stack STAC Collection URI"
    type:
      - https://raw.githubusercontent.com/eoap/schemas/main/string_format.yaml#URI
      - "null"
outputs: {}
steps: {}
hints:
  - class: eoap:RegoPolicyHint
    module: |
      package workflow

      deny contains "stack-uri must be provided" if {
        input["stack-uri"] == null
      }

      deny contains "stack-uri must start with http:// or https://" if {
        uri := input["stack-uri"]
        uri != null
        not startswith(uri, "http://")
        not startswith(uri, "https://")
      }
    queries:
      - data.workflow.deny[_]
