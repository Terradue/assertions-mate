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

from . import (
    JSONSchemaHint,
    RegoPolicyHint,
    Cql2FilterHint,
    extract_assertion_hints
)
from cwl2ogc import BaseCWLtypes2OGCConverter
from cwl_utils.parser import load_document_by_uri
from cwl_utils.parser.cwl_v1_2 import Workflow
from datetime import datetime
from loguru import logger
from pathlib import Path
from typing import (
    Any,
    Mapping
)

import click
import yaml
import time

def _scan_workflow(
    wf: Workflow,
    inputs: Mapping[str, Any]
):
    logger.info('------------------------------------------------------------------------')
    workflow_id = wf.id.split('#')[-1]
    logger.info(f"Validating #{workflow_id} {wf.class_} ({wf.cwlVersion}):")

    validators = []

    # prepare
    for hint_instance in extract_assertion_hints(wf):
        logger.info(f"Setting up validator for {type(hint_instance).__name__}...")

        try:
            validators.append(hint_instance.validator())
        except Exception as e:
            logger.error(f"An error occurred when setting up {type(hint_instance).__name__}: {e}")

    if validators:
        logger.info("Setup is over, validating...")

        for validator in validators:
            logger.info(f"  - Executing {type(validator).__name__}...")

            problem_details = validator.validate_inputs(inputs)
            if problem_details:
                logger.error(f"    {type(validator).__name__} detected violations below:")

                for error_detail in problem_details.errors:
                    logger.error(f"    [{error_detail.pointer}] {error_detail.detail}")
            else:
                logger.info(f"    {type(validator).__name__} execution terminated with no violations")
    else:
        logger.info(f"No Validators configured in '#{workflow_id}.hints'")

@click.command()
@click.argument(
    'workflow',
    type=click.Path(
        path_type=Path,
        exists=True,
        readable=True,
        resolve_path=True
    ),
    required=True
)
@click.option(
    '--inputs',
    type=click.Path(
        path_type=Path,
        exists=True,
        readable=True,
        resolve_path=True
    ),
    required=True,
    help="The Workflow inputs to check against the input Workflow"
)
def main(
    workflow: Path,
    inputs: Path
):
    start_time = time.time()

    logger.info(f"Loading CWL document from {workflow.absolute()}")

    cwl_document = load_document_by_uri(
        path=workflow,
        load_all=True
    )

    end_time = time.time()
    logger.info(f"{workflow.absolute()} load in {end_time - start_time:.4f} seconds")

    logger.info(f"Loading inputs from {inputs.absolute()}")

    with inputs.open() as input_stream:
        inputs_mapping = yaml.safe_load(input_stream)

    if isinstance(cwl_document, list):
        for wf in cwl_document:
            _scan_workflow(wf, inputs_mapping)                
    else:
        _scan_workflow(cwl_document, inputs_mapping)

    end_time = time.time()

    logger.info('------------------------------------------------------------------------')
    logger.info('VALIDATION COMPLETE')
    logger.info('------------------------------------------------------------------------')

    logger.info(f"Total time: {end_time - start_time:.4f} seconds")
    logger.info(f"Finished at: {datetime.fromtimestamp(end_time).isoformat(timespec='milliseconds')}")
