cwlVersion: v1.2
class: Workflow
id: optional-input-validation
inputs:
  optional-code:
    type:
      - string
      - "null"
outputs: {}
steps: {}
hints:
  - class: eoap:RegoPolicyHint
    module: |
      package workflow

      deny[msg] {
        v := input["optional-code"]
        v != null
        not regex.match("^[A-Z]{3}$", v)
        msg := "optional-code must be 3 uppercase letters"
      }
    queries:
      - data.workflow.deny[_]
