# CLI Reference

## Installation

Starting with version `0.9.0`, the CLI dependencies are optional. Install the
package with the `cli` extra to use the `assertions-mate` command:

```bash
pip install "assertions-mate[cli]"
```

For an editable installation from source, use:

```bash
pip install -e ".[cli]"
```

## Command

```bash
assertions-mate WORKFLOW --inputs INPUTS
```

## Arguments

- `WORKFLOW` (required): path to a CWL workflow file

## Options

- `--inputs` (required): path to input values (YAML)

## Behavior

1. Loads CWL document(s) from `WORKFLOW`.
2. Extracts supported assertion hints from each workflow's `hints`.
3. Builds validator instances from each hint.
4. Validates provided `INPUTS`.
5. Logs all violations.

## Execution Model

- Hint setup is best-effort per hint type.
- If one hint fails during setup, others can still run.
- Violations are reported by validator as structured log lines.

## Error Classes

- CWL load/parse errors: command stops before validation.
- Hint setup errors: failing hint is skipped, process continues.
- Validation violations: reported per validator and per rule/query pointer.

## Exit and Output Notes

- The command emits validation information through logs.
- Validation failures are reported as error log lines that include pointer and detail text.
- Current behavior may still complete with exit code `0` when violations are reported; use log inspection in automation if strict failure semantics are required.
