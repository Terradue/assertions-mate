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
id: disjoint-geometries-validation
inputs:
  g1:
    type: https://raw.githubusercontent.com/eoap/schemas/main/geojson.yaml#Polygon
  g2:
    type: https://raw.githubusercontent.com/eoap/schemas/main/geojson.yaml#Polygon
outputs: {}
steps: {}
hints:
  - class: eoap:Cql2FilterHint
    queries:
      - id: geometries-disjoint
        cql2: "s_disjoint(ensure_spatial(g1), ensure_spatial(g2))"
        message: "g1 and g2 must be disjoint"
