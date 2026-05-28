# Testing and Reliability

This project benefits from a split testing strategy.

## Unit Tests

Focus on deterministic behavior with local types and direct validator logic.

Examples:
- hint extraction and mapping tests
- CQL2 text/json predicate tests
- JSON schema validation tests

## Integration-Oriented Tests

Use real example workflows and external type references.

Because these can require network and parser compatibility, they should:
- skip when offline
- be isolated from core deterministic tests

## Reliability Patterns for CI

- treat hint setup errors as first-class signals
- include at least one valid and one invalid case per how-to example
- prefer stable syntax subsets for Rego and CQL2 in production pipelines

## Practical Guardrails

- keep payload key names aligned with workflow inputs
- document scalar vs wrapped object shapes (`value`) and test both where applicable
- reuse proven example expressions to avoid backend incompatibilities
