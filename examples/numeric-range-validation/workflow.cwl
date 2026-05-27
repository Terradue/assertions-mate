cwlVersion: v1.2
class: Workflow
id: numeric-range-validation
inputs:
  count:
    type: int
outputs: {}
steps: {}
hints:
  - class: eoap:RegoPolicyHint
    module: |
      package workflow

      deny[msg] {
        c := input["count"]
        c < 1
        msg := "count must be >= 1"
      }

      deny[msg] {
        c := input["count"]
        c > 10
        msg := "count must be <= 10"
      }
    queries:
      - data.workflow.deny[_]
