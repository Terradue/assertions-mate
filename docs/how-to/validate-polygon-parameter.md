# How-to: Validate a CWL Polygon Parameter

This guide shows how to validate a CWL input parameter representing a GeoJSON `Polygon` using `eoap:Cql2FilterHint`.

## 1. Define the CWL input (packed workflow style)

Use a packed CWL with `$graph` and `SchemaDefRequirement` imports:

```yaml
cwlVersion: v1.2
$graph:
  - class: Workflow
    id: s1-coherence-intensity
    requirements:
      - class: SchemaDefRequirement
        types:
          - $import: https://raw.githubusercontent.com/eoap/schemas/main/string_format.yaml
          - $import: https://raw.githubusercontent.com/eoap/schemas/main/geojson.yaml
    inputs:
      aoi:
        type:
          - https://raw.githubusercontent.com/eoap/schemas/main/geojson.yaml#Polygon
          - "null"
```

`assertions-mate` validates values from the input payload, and CQL2 rules can enforce required conditions.

## 2. Add CQL2 checks for Polygon

Add this hint under `hints:` in your workflow:

```yaml
hints:
  - class: eoap:Cql2FilterHint
    queries:
      - id: polygon-type
        cql2: "aoi.type = 'Polygon'"
        message: "aoi.type must be Polygon"
      - id: polygon-bbox-presence
        cql2: "aoi.bbox IS NOT NULL"
        message: "aoi.bbox must be provided"
```

This enforces that the input is a Polygon and includes a bbox.

## 3. Validate with a sample value

Create `inputs.yaml`:

```yaml
aoi:
  type: Polygon
  coordinates:
    - - [-91.26192176217288, -0.5548429855061556]
      - [-90.9516940668717, -0.5548429855061556]
      - [-90.9516940668717, -0.34012874412405836]
      - [-91.26192176217288, -0.34012874412405836]
      - [-91.26192176217288, -0.5548429855061556]
  bbox: [-91.26192176217288, -0.5548429855061556, -90.9516940668717, -0.34012874412405836]
```

Run validation:

```bash
assertions-mate workflow.cwl --inputs inputs.yaml
```

## Ready-to-run example in this repository

You can run the prepared files in:

- `examples/polygon-validation/workflow.cwl`
- `examples/polygon-validation/inputs-valid.yaml`
- `examples/polygon-validation/inputs-invalid.yaml`

## 4. Optional: strict schema validation

If you need full structural validation against EOAP GeoJSON schema (`coordinates` nesting, numeric constraints, etc.), use a `JSONSchemaHint` based on:

- `https://github.com/eoap/schemas/blob/main/geojson.yaml`

Use CQL2 for predicate-style rules, and JSON Schema when you need strict object-shape validation.
