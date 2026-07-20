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
id: reusable-rego-snippets
inputs:
  start-date:
    type: string
  end-date:
    type: string
outputs: {}
steps: {}
hints:
  - class: eoap:RegoPolicyHint
    module: |
      package workflow

      is_rfc3339_utc(s) {
        regex.match("^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$", s)
      }

      deny[msg] {
        s := input["start-date"]
        not is_rfc3339_utc(s)
        msg := "start-date format is invalid"
      }

      deny[msg] {
        e := input["end-date"]
        not is_rfc3339_utc(e)
        msg := "end-date format is invalid"
      }
    queries:
      - data.workflow.deny[_]
