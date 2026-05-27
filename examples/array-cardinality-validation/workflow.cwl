cwlVersion: v1.2
class: Workflow
id: array-cardinality-validation
inputs:
  items:
    type: string[]
outputs: {}
steps: {}
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
