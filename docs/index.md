# Assertions Mate Documentation

`assertions-mate` validates CWL workflow inputs against assertion hints embedded in workflow definitions.

It supports three validation families:

- JSON Schema
- Rego policy queries (OPA)
- CQL2 filter expressions

## Start Here

If you are new, follow this path:

1. [Build your first validated workflow](tutorials/first-validated-workflow.md)
2. Run a ready example:
   `assertions-mate examples/.../workflow.cwl --inputs examples/.../inputs-valid.yaml`
3. Pick a task-specific guide from `How-to`

## Most Used Guides

- [Validate Polygon Parameter](how-to/validate-polygon-parameter.md)
- [Validate URI Input](how-to/validate-uri-input.md)
- [Validate Datetime Input](how-to/validate-datetime-input.md)
- [Validate Date Range Input](how-to/validate-date-range-inputs.md)
- [Validate Point In Polygon (CQL2)](how-to/validate-point-in-polygon-cql2.md)

## Docs By Purpose

- Tutorials: step-by-step learning
- How-to Guides: task-oriented recipes
- Reference: exact contracts and behavior
- Explanation: rationale, compatibility, and limits

Quick links:
- [CLI Reference](reference/cli.md)
- [Hint Reference](reference/hints.md)
- [Runtime Compatibility](reference/runtime-compatibility.md)
- [Architecture](explanation/architecture.md)

## When Things Fail

- Rego syntax/runtime issues: [Troubleshoot Rego Invalid Literal](how-to/troubleshoot-rego-invalid-literal.md)
- CWL load/parse issues: [Troubleshoot CWL Loader Errors](how-to/troubleshoot-cwl-loader-errors.md)
