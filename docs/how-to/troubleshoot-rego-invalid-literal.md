# How-to: Troubleshoot Rego "Invalid literal" Errors

If you see errors around `deny contains ... if { ... }`, your runtime is parsing classic Rego syntax.

## Symptoms

- `Invalid literal`
- `wellformed_error`
- validator setup fails for `RegoPolicyHint`

## Fix

Use classic syntax:

```rego
deny[msg] {
  input["x"] == null
  msg := "x is required"
}
```

instead of:

```rego
deny contains "x is required" if {
  input["x"] == null
}
```

## Verify

Run your workflow and ensure `Setting up validator for RegoPolicyHint...` completes without parser errors.
