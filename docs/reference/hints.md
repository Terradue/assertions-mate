# Hint Reference

`assertions-mate` maps `eoap:` hint classes to validator implementations.

## Input Payload Shape

Hint evaluation uses keys from the runtime input mapping.
Your YAML input keys must match workflow input names exactly.

Example mismatch:
- workflow input: `input-uri`
- payload key: `stack-uri`

This can produce false-negative validations because rules read missing keys.

## `eoap:JSONSchemaHint`

- Purpose: validate input payload with JSON Schema
- [Schema](hints_schema.html#JSONSchemaHint)
- Fields:
  - `json_schema` (object): JSON Schema definition for the input payload
- Notes:
  - structural constraints are explicit and deterministic
  - useful for required fields, enums, cardinality, and numeric bounds

## `eoap:RegoPolicyHint`

- Purpose: evaluate business or policy constraints with Rego
- [Schema](hints_schema.html#RegoPolicyHint)
- Fields:
  - `module` (string): Rego module source text
  - `queries` (list of string): query expressions to evaluate
- Recommended syntax:

```rego
deny[msg] {
  condition
  msg := "..."
}
```

- Recommended query:

```text
data.workflow.deny[_]
```

- Compatibility note:
  - newer `deny contains ... if { ... }` syntax can fail in some runtimes with `Invalid literal`

## `eoap:Cql2FilterHint`

- Purpose: enforce boolean checks expressed as CQL2 filters
- [Schema](hints_schema.html#Cql2FilterHint)
- Fields:
  - `custom_functions` (string): Optional Python custom function(s) definition
  - `queries` (list):
    - `id` (string): rule identifier
    - `cql2` (string or object): CQL2 text or CQL2 JSON
    - `message` (string): error message when filter evaluates to false
