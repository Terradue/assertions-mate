# Copyright 2025 Terradue
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

cwlVersion: v1.2
class: Workflow
id: polygon-aoi
requirements:
  - class: SchemaDefRequirement
    types:
      - $import: https://raw.githubusercontent.com/eoap/schemas/main/string_format.yaml
      - $import: https://raw.githubusercontent.com/eoap/schemas/main/geojson.yaml
inputs:
  aoi:
    label: Area of interest
    doc: Area of interest
    type: https://raw.githubusercontent.com/eoap/schemas/main/geojson.yaml#Polygon
outputs: {}
steps: {}
hints:
  - class: eoap:Cql2FilterHint
    queries:
      - id: aoi-present
        cql2: "aoi IS NOT NULL"
        message: "aoi must be provided"
      - id: aoi-type-is-polygon
        cql2: "aoi.type = 'Polygon'"
        message: "aoi.type must be Polygon"
      - id: aoi-bbox-present
        cql2: "aoi.bbox IS NOT NULL"
        message: "aoi.bbox must be provided"
