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
id: datetime-validation
label: Datetime Input Validation
doc: Validate datetime-like inputs for EOAP workflows.
requirements:
  - class: SchemaDefRequirement
    types:
      - $import: https://raw.githubusercontent.com/eoap/schemas/main/string_format.yaml
inputs:
  sensing-time:
    id: sensing-time
    label: "Sensing time"
    doc: "Acquisition datetime"
    type:
      - https://raw.githubusercontent.com/eoap/schemas/main/string_format.yaml#DateTime
      - "null"
outputs: {}
steps: {}
hints:
  - class: eoap:RegoPolicyHint
    module: |
      package workflow

      deny[msg] {
        input["sensing-time"] == null
        msg := "sensing-time must be provided"
      }

      deny[msg] {
        st := input["sensing-time"]
        st != null
        st["value"] == null
        msg := "sensing-time.value must be provided"
      }

      deny[msg] {
        st := input["sensing-time"]
        st != null
        t := st["value"]
        t != null
        not regex.match("^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$", t)
        msg := "sensing-time must be UTC RFC3339 like YYYY-MM-DDTHH:MM:SSZ"
      }
    queries:
      - data.workflow.deny[_]
