# CLI Reference

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

## Exit and Output Notes

- The command emits validation information through logs.
- Validation failures are reported as error log lines that include pointer and detail text.
