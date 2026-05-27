# How-to: Create Reusable Rego Snippets

Keep common checks reusable by copying a shared module block between workflows.

## 1. Define the inputs

```yaml
inputs:
  start-date:
    type: string
  end-date:
    type: string
```

## 2. Add reusable Rego helper

```rego
package workflow

is_rfc3339_utc(s) {
  regex.match("^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$", s)
}
```

Then reuse in multiple deny rules.

## 3. Add hint using the helper

```yaml
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
    queries:
      - data.workflow.deny[_]
```

## Ready-to-run example in this repository

- `examples/reusable-rego-snippets/workflow.cwl`
- `examples/reusable-rego-snippets/inputs-valid.yaml`
- `examples/reusable-rego-snippets/inputs-invalid.yaml`
