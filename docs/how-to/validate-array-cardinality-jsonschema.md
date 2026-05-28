# How-to: Validate Array Cardinality (JSON Schema)

Require `items` array length between 1 and 3.

## 1. Define the input

```yaml
inputs:
  items:
    type: string[]
```

## 2. Add JSON Schema hint

```yaml
hints:
  - class: eoap:JSONSchemaHint
    json_schema:
      type: object
      required: [items]
      properties:
        items:
          type: array
          minItems: 1
          maxItems: 3
          items:
            type: string
```

## 3. Validate with sample values

Valid:

```yaml
items: ["a", "b"]
```

Run:

```bash
assertions-mate workflow.cwl --inputs inputs-valid.yaml
```

## Ready-to-run example in this repository

- `examples/array-cardinality-validation/workflow.cwl`
- `examples/array-cardinality-validation/inputs-valid.yaml`
- `examples/array-cardinality-validation/inputs-invalid.yaml`
