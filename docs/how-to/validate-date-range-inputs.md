# How-to: Assert `end-date` Is Greater Than `start-date`

This guide shows how to validate two datetime inputs so that `end-date` is strictly greater than `start-date`.

## 1. Define the inputs

```yaml
inputs:
  start-date:
    type:
      - string
      - "null"
  end-date:
    type:
      - string
      - "null"
```

## 2. Add Rego checks

```yaml
hints:
  - class: eoap:RegoPolicyHint
    module: |
      package workflow

      deny[msg] {
        input["start-date"] == null
        msg := "start-date must be provided"
      }

      deny[msg] {
        input["end-date"] == null
        msg := "end-date must be provided"
      }

      # RFC3339 UTC format (YYYY-MM-DDTHH:MM:SSZ)
      deny[msg] {
        s := input["start-date"]
        s != null
        not regex.match("^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$", s)
        msg := "start-date must be UTC RFC3339 like YYYY-MM-DDTHH:MM:SSZ"
      }

      deny[msg] {
        e := input["end-date"]
        e != null
        not regex.match("^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$", e)
        msg := "end-date must be UTC RFC3339 like YYYY-MM-DDTHH:MM:SSZ"
      }

      deny[msg] {
        s := input["start-date"]
        e := input["end-date"]
        regex.match("^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$", s)
        regex.match("^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$", e)
        e <= s
        msg := "end-date must be greater than start-date"
      }
    queries:
      - data.workflow.deny[_]
```

Because both values use the same UTC RFC3339 shape, lexicographic string comparison is safe for ordering.

## 3. Run

```bash
assertions-mate path/to/workflow.cwl --inputs path/to/inputs.yaml
```

## Ready-to-run example in this repository

- `examples/date-range-validation/workflow.cwl`
- `examples/date-range-validation/inputs-valid.yaml`
- `examples/date-range-validation/inputs-invalid.yaml`
- `examples/date-range-validation/inputs-null.yaml`
