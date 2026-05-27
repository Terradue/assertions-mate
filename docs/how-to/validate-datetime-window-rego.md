# How-to: Validate DateTime Window With Rego

Validate that `end-date` is greater than `start-date` and both are in UTC RFC3339 format.

## 1. Define the inputs

```yaml
inputs:
  start-date:
    type: string
  end-date:
    type: string
```

## 2. Add Rego checks

```yaml
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
```

## 3. Validate with sample values

Valid:

```yaml
start-date: "2026-05-27T10:00:00Z"
end-date: "2026-05-27T11:00:00Z"
```

Run:

```bash
assertions-mate workflow.cwl --inputs inputs-valid.yaml
```

## Ready-to-run example in this repository

- `examples/datetime-window-validation/workflow.cwl`
- `examples/datetime-window-validation/inputs-valid.yaml`
- `examples/datetime-window-validation/inputs-invalid.yaml`
