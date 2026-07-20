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
id: multi-hint-validation
inputs:
  count:
    type: int
  aoi:
    type: https://raw.githubusercontent.com/eoap/schemas/main/geojson.yaml#Polygon
  candidate:
    type: https://raw.githubusercontent.com/eoap/schemas/main/geojson.yaml#Polygon
outputs: {}
steps: {}
hints:
  - class: eoap:JSONSchemaHint
    json_schema:
      type: object
      required: [count, aoi, candidate]
      properties:
        count:
          type: integer
          minimum: 1
  - class: eoap:RegoPolicyHint
    module: |
      package workflow

      deny[msg] {
        input["count"] > 10
        msg := "count must be <= 10"
      }
    queries:
      - data.workflow.deny[_]
  - class: eoap:Cql2FilterHint
    queries:
      - id: polygons-intersect
        cql2: "s_intersects(ensure_spatial(candidate), ensure_spatial(aoi))"
        message: "candidate must intersect aoi"
