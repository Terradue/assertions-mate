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
id: datetime-window-validation
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

      deny[msg] {
        s := input["start-date"]
        not regex.match("^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$", s)
        msg := "start-date must be UTC RFC3339 like YYYY-MM-DDTHH:MM:SSZ"
      }

      deny[msg] {
        e := input["end-date"]
        not regex.match("^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$", e)
        msg := "end-date must be UTC RFC3339 like YYYY-MM-DDTHH:MM:SSZ"
      }

      deny[msg] {
        s := input["start-date"]
        e := input["end-date"]
        e <= s
        msg := "end-date must be greater than start-date"
      }
    queries:
      - data.workflow.deny[_]
