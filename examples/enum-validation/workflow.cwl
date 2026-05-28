cwlVersion: v1.2
class: Workflow
id: enum-validation
inputs:
  mode:
    type: string
outputs: {}
steps: {}
hints:
  - class: eoap:JSONSchemaHint
    json_schema:
      type: object
      required: [mode]
      properties:
        mode:
          type: string
          enum: [fast, strict]
