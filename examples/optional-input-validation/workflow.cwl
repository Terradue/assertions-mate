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
id: optional-input-validation
inputs:
  optional-code:
    type:
      - string
      - "null"
outputs: {}
steps: {}
hints:
  - class: eoap:RegoPolicyHint
    module: |
      package workflow

      deny[msg] {
        v := input["optional-code"]
        v != null
        not regex.match("^[A-Z]{3}$", v)
        msg := "optional-code must be 3 uppercase letters"
      }
    queries:
      - data.workflow.deny[_]
