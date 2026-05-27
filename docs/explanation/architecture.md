# Architecture and Design

`assertions-mate` is built around hint-driven validation for CWL workflows.

## Why Hints

CWL input typing can enforce structure, but many operational constraints are semantic:
- policy constraints
- domain rules
- geospatial relationships

Hints let these constraints travel with workflow definitions and be checked consistently before runtime.

## Validation Flow

1. Load CWL workflow document(s).
2. Read `workflow.hints`.
3. Map supported `eoap:*` hint classes to typed hint models.
4. Build validator objects from hints.
5. Run each validator against provided inputs.
6. Aggregate and log violations.

## Validator Model

Each hint type is responsible for producing a validator via `.validator()`.

This keeps:
- hint parsing and serialization concerns in hint models
- runtime validation behavior in validator classes

## Supported Rule Languages

- JSON Schema: structural constraints over payload shape and values
- Rego: policy-oriented queries and rich rule composition
- CQL2: declarative predicate checks, including geospatial expressions
