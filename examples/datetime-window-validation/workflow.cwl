cwlVersion: v1.2
class: Workflow
id: datetime-window-validation
inputs:
  start-date:
    type: string
  end-date:
    type: string
outputs: {}
steps: {}
hints:
  - class: eoap:RegoPolicyHint
    module: |
      package workflow

      deny[msg] {
        s := input["start-date"]
        not regex.match("^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$", s)
        msg := "start-date must be UTC RFC3339 like YYYY-MM-DDTHH:MM:SSZ"
      }

      deny[msg] {
        e := input["end-date"]
        not regex.match("^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$", e)
        msg := "end-date must be UTC RFC3339 like YYYY-MM-DDTHH:MM:SSZ"
      }

      deny[msg] {
        s := input["start-date"]
        e := input["end-date"]
        e <= s
        msg := "end-date must be greater than start-date"
      }
    queries:
      - data.workflow.deny[_]
