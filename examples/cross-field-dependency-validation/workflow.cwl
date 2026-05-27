cwlVersion: v1.2
class: Workflow
id: cross-field-dependency-validation
inputs:
  mode:
    type: string
  threshold:
    type:
      - int
      - "null"
outputs: {}
steps: {}
hints:
  - class: eoap:RegoPolicyHint
    module: |
      package workflow

      deny[msg] {
        input["mode"] == "strict"
        input["threshold"] == null
        msg := "threshold is required when mode is strict"
      }
    queries:
      - data.workflow.deny[_]
