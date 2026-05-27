# How-to: Assert `end-date` Is Greater Than `start-date`

This guide shows how to validate two datetime inputs so that `end-date` is strictly greater than `start-date`.

## 1. Define the inputs

```yaml
inputs:
  start-date:
    type: https://raw.githubusercontent.com/eoap/schemas/main/string_format.yaml#DateTime
  end-date:
    type: https://raw.githubusercontent.com/eoap/schemas/main/string_format.yaml#DateTime
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
        sd := input["start-date"]
        sd != null
        sd["value"] == null
        msg := "start-date.value must be provided"
      }

      deny[msg] {
        input["end-date"] == null
        msg := "end-date must be provided"
      }

      deny[msg] {
        ed := input["end-date"]
        ed != null
        ed["value"] == null
        msg := "end-date.value must be provided"
      }

      deny[msg] {
        sd := input["start-date"]
        ed := input["end-date"]
        sd != null
        ed != null
        s := sd["value"]
        e := ed["value"]
        regex.match("^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$", s)
        regex.match("^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$", e)
        e <= s
        msg := "end-date must be greater than start-date"
      }
    queries:
      - data.workflow.deny[_]
```

Because both values use the same UTC RFC3339 shape, lexicographic string comparison is safe for ordering.

## 3. Validate with sample values

Valid payload shape:

```yaml
start-date:
  value: "2026-05-27T10:00:00Z"
end-date:
  value: "2026-05-27T12:00:00Z"
```

```bash
assertions-mate path/to/workflow.cwl --inputs path/to/inputs.yaml
```

## Ready-to-run example in this repository

- `examples/date-range-validation/workflow.cwl`
- `examples/date-range-validation/inputs-valid.yaml`
- `examples/date-range-validation/inputs-invalid.yaml`
- `examples/date-range-validation/inputs-null.yaml`
