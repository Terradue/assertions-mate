# How-to: Validate a CWL URI Input

This guide shows how to validate a URI input using `eoap:RegoPolicyHint`.

## 1. Define the URI input

```yaml
cwlVersion: v1.2
class: Workflow
id: uri-validation
inputs:
  input-uri:
    id: input-uri
    label: "Input URI"
    doc: "Input URI to validate"
    type:
      - https://raw.githubusercontent.com/eoap/schemas/main/string_format.yaml#URI
      - "null"
```

## 2. Add Rego policy checks

Add validation checks under `hints:`:

```yaml
hints:
  - class: eoap:RegoPolicyHint
    module: |
      package workflow

      deny[msg] {
        input["input-uri"] == null
        msg := "input-uri must be provided"
      }

      deny[msg] {
        iu := input["input-uri"]
        iu != null
        iu["value"] == null
        msg := "input-uri.value must be provided"
      }

      deny[msg] {
        iu := input["input-uri"]
        iu != null
        uri := iu["value"]
        uri != null
        not startswith(uri, "http://")
        not startswith(uri, "https://")
        msg := "input-uri must start with http:// or https://"
      }
    queries:
      - data.workflow.deny[_]
```

## 3. Validate with sample inputs

Valid input:

```yaml
input-uri:
  value: "https://earth-search.aws.element84.com/v1/collections/sentinel-1-grd"
```

Run:

```bash
assertions-mate workflow.cwl --inputs inputs-valid.yaml
```

## Ready-to-run example in this repository

Use these files directly:

- `examples/uri-validation/workflow.cwl`
- `examples/uri-validation/inputs-valid.yaml`
- `examples/uri-validation/inputs-invalid.yaml`
- `examples/uri-validation/inputs-null.yaml`
