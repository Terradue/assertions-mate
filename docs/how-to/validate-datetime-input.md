# How-to: Validate a CWL Datetime Input

This guide shows how to validate a datetime input using `eoap:RegoPolicyHint`.

## 1. Define the input

If your environment supports external schema references, use:

```yaml
inputs:
  sensing-time:
    id: sensing-time
    label: "Sensing time"
    doc: "Acquisition datetime"
    type:
      - https://raw.githubusercontent.com/eoap/schemas/main/string_format.yaml#Datetime
      - "null"
```

If your CWL parser rejects external typed references in this context, use `string` and validate format via policy:

```yaml
inputs:
  sensing-time:
    id: sensing-time
    label: "Sensing time"
    doc: "Acquisition datetime"
    type:
      - string
      - "null"
```

## 2. Add Rego checks

Add this under `hints:`:

```yaml
hints:
  - class: eoap:RegoPolicyHint
    module: |
      package workflow

      deny[msg] {
        input["sensing-time"] == null
        msg := "sensing-time must be provided"
      }

      # Basic RFC3339-like check: 2026-05-27T16:20:00Z
      deny[msg] {
        t := input["sensing-time"]
        t != null
        not regex.match("^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$", t)
        msg := "sensing-time must be UTC RFC3339 like YYYY-MM-DDTHH:MM:SSZ"
      }
    queries:
      - data.workflow.deny[_]
```

## 3. Example inputs

Valid:

```yaml
sensing-time: "2026-05-27T16:20:00Z"
```

Invalid:

```yaml
sensing-time: "2026/05/27 16:20:00"
```

## 4. Run

```bash
assertions-mate path/to/workflow.cwl --inputs path/to/inputs.yaml
```

## Ready-to-run example in this repository

Use these files directly:

- `examples/datetime-validation/workflow.cwl`
- `examples/datetime-validation/inputs-valid.yaml`
- `examples/datetime-validation/inputs-invalid.yaml`
- `examples/datetime-validation/inputs-null.yaml`
