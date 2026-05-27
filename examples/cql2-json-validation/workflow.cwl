cwlVersion: v1.2
class: Workflow
id: cql2-json-validation
inputs:
  mode:
    type: string
outputs: {}
steps: {}
hints:
  - class: eoap:Cql2FilterHint
    queries:
      - id: mode-is-strict
        cql2:
          op: "="
          args:
            - property: mode
            - "strict"
        message: "mode must be strict"
