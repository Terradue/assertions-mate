cwlVersion: v1.2
class: Workflow
id: datetime-validation
label: Datetime Input Validation
doc: Validate datetime-like inputs for EOAP workflows.
requirements:
  - class: SchemaDefRequirement
    types:
      - $import: https://raw.githubusercontent.com/eoap/schemas/main/string_format.yaml
inputs:
  sensing-time:
    id: sensing-time
    label: "Sensing time"
    doc: "Acquisition datetime"
    type:
      - https://raw.githubusercontent.com/eoap/schemas/main/string_format.yaml#DateTime
      - "null"
outputs: {}
steps: {}
hints:
  - class: eoap:RegoPolicyHint
    module: |
      package workflow

      deny[msg] {
        input["sensing-time"] == null
        msg := "sensing-time must be provided"
      }

      deny[msg] {
        t := input["sensing-time"]
        t != null
        not regex.match("^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$", t)
        msg := "sensing-time must be UTC RFC3339 like YYYY-MM-DDTHH:MM:SSZ"
      }
    queries:
      - data.workflow.deny[_]
