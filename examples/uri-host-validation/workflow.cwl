cwlVersion: v1.2
class: Workflow
id: uri-host-validation
inputs:
  input-uri:
    type: string
outputs: {}
steps: {}
hints:
  - class: eoap:RegoPolicyHint
    module: |
      package workflow

      deny[msg] {
        uri := input["input-uri"]
        not startswith(uri, "https://")
        msg := "input-uri must start with https://"
      }

      deny[msg] {
        uri := input["input-uri"]
        not startswith(uri, "https://earth-search.aws.element84.com/")
        msg := "input-uri must target earth-search.aws.element84.com"
      }
    queries:
      - data.workflow.deny[_]
