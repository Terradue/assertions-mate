# How-to: Validate URI Host Constraints (Rego)

Validate URI inputs with host/path policies.

## 1. Define the input

```yaml
inputs:
  input-uri:
    type: string
```

## 2. Add Rego checks

- require `https://`
- require host prefix `earth-search.aws.element84.com/`

```yaml
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
```

## 3. Validate with sample values

Valid:

```yaml
input-uri: "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a"
```

Run:

```bash
assertions-mate workflow.cwl --inputs inputs-valid.yaml
```

## Ready-to-run example in this repository

- `examples/uri-host-validation/workflow.cwl`
- `examples/uri-host-validation/inputs-valid.yaml`
- `examples/uri-host-validation/inputs-invalid.yaml`
