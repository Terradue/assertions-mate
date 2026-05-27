# How-to: Use Packed CWL vs Single Workflow CWL

## Single workflow

Best for local examples and fast validation loops.

```yaml
cwlVersion: v1.2
class: Workflow
id: my-workflow
...
```

## Packed workflow (`$graph`)

Useful when distributing multiple process definitions in one file.

```yaml
cwlVersion: v1.2
$graph:
  - class: Workflow
    id: my-workflow
    ...
```

## Recommendation

Start with single-workflow CWL for validator docs/examples, then move to packed CWL once parser compatibility is confirmed in your target runtime.
