# How-to: Validate Enum Values (JSON Schema)

Use `enum` to restrict allowed values.

## 1. Define the input

```yaml
inputs:
  mode:
    type: string
```

## 2. Add JSON Schema hint

```yaml
hints:
  - class: eoap:JSONSchemaHint
    json_schema:
      type: object
      required: [mode]
      properties:
        mode:
          type: string
          enum: [fast, strict]
```

## 3. Validate with sample values

Valid:

```yaml
mode: "strict"
```

Run:

```bash
assertions-mate workflow.cwl --inputs inputs-valid.yaml
```

## Ready-to-run example in this repository

- `examples/enum-validation/workflow.cwl`
- `examples/enum-validation/inputs-valid.yaml`
- `examples/enum-validation/inputs-invalid.yaml`
