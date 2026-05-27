# How-to: Validate a CWL URI Input

This guide shows how to validate a URI input using a packed CWL workflow and `eoap:RegoPolicyHint`.

## 1. Define the URI input

```yaml
cwlVersion: v1.2
class: Workflow
id: uri-validation
inputs:
  stack-uri:
    id: stack-uri
    label: "Snapping Stack URI"
    doc: "SNAPPING Stack STAC Collection URI"
    type:
      - string
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
        input["stack-uri"] == null
        msg := "stack-uri must be provided"
      }

      deny[msg] {
        uri := input["stack-uri"]
        uri != null
        not startswith(uri, "http://")
        not startswith(uri, "https://")
        msg := "stack-uri must start with http:// or https://"
      }
    queries:
      - data.workflow.deny[_]
```

## 3. Validate with sample inputs

Valid input:

```yaml
stack-uri: "https://earth-search.aws.element84.com/v1/collections/sentinel-1-grd"
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
