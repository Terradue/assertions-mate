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
id: uri-validation
label: URI Input Validation
doc: Validate URI-like inputs for EOAP workflows.
requirements:
  - class: SchemaDefRequirement
    types:
      - $import: https://raw.githubusercontent.com/eoap/schemas/main/string_format.yaml
inputs:
  input-uri:
    id: input-uri
    type:
      - https://raw.githubusercontent.com/eoap/schemas/main/string_format.yaml#URI
      - "null"
outputs: {}
steps: {}
hints:
  - class: eoap:RegoPolicyHint
    module: |
      package workflow

      deny[msg] {
        input["input-uri"] == null
        msg := "input-uri must be provided"
      }

      deny[msg] {
        iu := input["input-uri"]
        iu != null
        iu["value"] == null
        msg := "input-uri.value must be provided"
      }

      deny[msg] {
        iu := input["input-uri"]
        iu != null
        uri := iu["value"]
        uri != null
        not startswith(uri, "http://")
        not startswith(uri, "https://")
        msg := "input-uri must start with http:// or https://"
      }
    queries:
      - data.workflow.deny[_]
