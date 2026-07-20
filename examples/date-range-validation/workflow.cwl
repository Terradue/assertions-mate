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
id: date-range-validation
label: Date Range Validation
doc: Validate that end-date is greater than start-date.
requirements:
  - class: SchemaDefRequirement
    types:
      - $import: https://raw.githubusercontent.com/eoap/schemas/main/string_format.yaml
inputs:
  start-date:
    type: https://raw.githubusercontent.com/eoap/schemas/main/string_format.yaml#DateTime
    
  end-date:
    type: https://raw.githubusercontent.com/eoap/schemas/main/string_format.yaml#DateTime

outputs: {}
steps: {}
hints:
  - class: eoap:RegoPolicyHint
    module: |
      package workflow

      deny[msg] {
        input["start-date"] == null
        msg := "start-date must be provided"
      }

      deny[msg] {
        sd := input["start-date"]
        sd != null
        sd["value"] == null
        msg := "start-date.value must be provided"
      }

      deny[msg] {
        input["end-date"] == null
        msg := "end-date must be provided"
      }

      deny[msg] {
        ed := input["end-date"]
        ed != null
        ed["value"] == null
        msg := "end-date.value must be provided"
      }

      deny[msg] {
        sd := input["start-date"]
        sd != null
        s := sd["value"]
        s != null
        not regex.match("^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$", s)
        msg := "start-date must be UTC RFC3339 like YYYY-MM-DDTHH:MM:SSZ"
      }

      deny[msg] {
        ed := input["end-date"]
        ed != null
        e := ed["value"]
        e != null
        not regex.match("^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$", e)
        msg := "end-date must be UTC RFC3339 like YYYY-MM-DDTHH:MM:SSZ"
      }

      deny[msg] {
        sd := input["start-date"]
        ed := input["end-date"]
        sd != null
        ed != null
        s := sd["value"]
        e := ed["value"]
        regex.match("^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$", s)
        regex.match("^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$", e)
        e <= s
        msg := "end-date must be greater than start-date"
      }
    queries:
      - data.workflow.deny[_]
