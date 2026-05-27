# Hint Reference

`assertions-mate` maps `eoap:` hint classes to validator implementations.

## `eoap:JSONSchemaHint`

- Purpose: validate input payload with JSON Schema
- Fields:
  - `json_schema` (object): JSON Schema definition for the input payload

## `eoap:RegoPolicyHint`

- Purpose: evaluate business or policy constraints with Rego
- Fields:
  - `module` (string): Rego module source text
  - `queries` (list of string): query expressions to evaluate

## `eoap:Cql2FilterHint`

- Purpose: enforce boolean checks expressed as CQL2 filters
- Fields:
  - `queries` (list):
    - `id` (string): rule identifier
    - `cql2` (string or object): CQL2 text or CQL2 JSON
    - `message` (string): error message when filter evaluates to false
