cwlVersion: v1.2
class: Workflow
id: reusable-rego-snippets
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

      is_rfc3339_utc(s) {
        regex.match("^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$", s)
      }

      deny[msg] {
        s := input["start-date"]
        not is_rfc3339_utc(s)
        msg := "start-date format is invalid"
      }

      deny[msg] {
        e := input["end-date"]
        not is_rfc3339_utc(e)
        msg := "end-date format is invalid"
      }
    queries:
      - data.workflow.deny[_]
