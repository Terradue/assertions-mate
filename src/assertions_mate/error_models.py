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

from __future__ import annotations

from enum import Enum
from typing import List, Literal, Optional

from pydantic import BaseModel, Field, RootModel, conint, constr

class AssertionModel(BaseModel):

    # Default dumps to JSON-friendly types (URLs -> str, datetimes -> ISO, etc.)
    def model_dump(self, *args, **kwargs):
        kwargs.setdefault('exclude_none', True)
        kwargs.setdefault('mode', 'json')
        return super().model_dump(*args, **kwargs)

    def model_dump_json(self, *args, **kwargs):
        # stays consistent with model_dump default
        kwargs.setdefault('exclude_none', True)
        kwargs.setdefault('indent', None)
        return super().model_dump_json(*args, **kwargs)

class ErrorDetail(AssertionModel):
    detail: constr(max_length=4096) = Field(
        ...,
        description='A granular description on the specific error related to a body property, query parameter, path parameters, and/or header.',
    )
    pointer: Optional[constr(max_length=1024)] = Field(
        default=None,
        description='A JSON Pointer to a specific request body property that is the source of error.',
    )
    parameter: Optional[constr(max_length=1024)] = Field(
        default=None,
        description='The name of the query or path parameter that is the source of error.',
    )
    header: Optional[constr(max_length=1024)] = Field(
        default=None, description='The name of the header that is the source of error.'
    )
    code: Optional[constr(max_length=50)] = Field(
        default=None,
        description='A string containing additional provider specific codes to identify the error context.',
    )


class Type(Enum):
    about_blank = 'about:blank'
    https___problems_registry_smartbear_com_already_exists = (
        'https://problems-registry.smartbear.com/already-exists'
    )
    https___problems_registry_smartbear_com_bad_request = (
        'https://problems-registry.smartbear.com/bad-request'
    )
    https___problems_registry_smartbear_com_business_rule_violation = (
        'https://problems-registry.smartbear.com/business-rule-violation'
    )
    https___problems_registry_smartbear_com_forbidden = (
        'https://problems-registry.smartbear.com/forbidden'
    )
    https___problems_registry_smartbear_com_invalid_body_property_format = (
        'https://problems-registry.smartbear.com/invalid-body-property-format'
    )
    https___problems_registry_smartbear_com_invalid_body_property_value = (
        'https://problems-registry.smartbear.com/invalid-body-property-value'
    )
    https___problems_registry_smartbear_com_invalid_parameters = (
        'https://problems-registry.smartbear.com/invalid-parameters'
    )
    https___problems_registry_smartbear_com_invalid_request_header_format = (
        'https://problems-registry.smartbear.com/invalid-request-header-format'
    )
    https___problems_registry_smartbear_com_invalid_request_parameter_format = (
        'https://problems-registry.smartbear.com/invalid-request-parameter-format'
    )
    https___problems_registry_smartbear_com_invalid_request_parameter_value = (
        'https://problems-registry.smartbear.com/invalid-request-parameter-value'
    )
    https___problems_registry_smartbear_com_license_cancelled = (
        'https://problems-registry.smartbear.com/license-cancelled'
    )
    https___problems_registry_smartbear_com_license_expired = (
        'https://problems-registry.smartbear.com/license-expired'
    )
    https___problems_registry_smartbear_com_missing_body_property = (
        'https://problems-registry.smartbear.com/missing-body-property'
    )
    https___problems_registry_smartbear_com_missing_request_header = (
        'https://problems-registry.smartbear.com/missing-request-header'
    )
    https___problems_registry_smartbear_com_not_found = (
        'https://problems-registry.smartbear.com/not-found'
    )
    https___problems_registry_smartbear_com_server_error = (
        'https://problems-registry.smartbear.com/server-error'
    )
    https___problems_registry_smartbear_com_service_unavailable = (
        'https://problems-registry.smartbear.com/service-unavailable'
    )
    https___problems_registry_smartbear_com_unauthorized = (
        'https://problems-registry.smartbear.com/unauthorized'
    )
    https___problems_registry_smartbear_com_validation_error = (
        'https://problems-registry.smartbear.com/validation-error'
    )


class ProblemDetails(AssertionModel):
    type: Optional[Type] = Field(
        default=None, description='A URI reference that identifies the problem type.'
    )
    status: Optional[conint(ge=100, le=599)] = Field(
        default=None,
        description='The HTTP status code generated by the origin server for this occurrence of the problem.',
    )
    title: Optional[constr(max_length=1024)] = Field(
        default=None,
        description='A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.',
    )
    detail: constr(max_length=4096) = Field(
        ...,
        description='A human-readable explanation specific to this occurrence of the problem.',
    )
    instance: Optional[constr(max_length=1024)] = Field(
        default=None,
        description='A URI reference that identifies the specific occurrence of the problem. It may or may not yield further information if dereferenced.',
    )
    code: Optional[constr(max_length=50)] = Field(
        default=None,
        description='An API specific error code aiding the provider team understand the error based on their own potential taxonomy or registry.',
    )
    errors: Optional[List[ErrorDetail]] = Field(
        default=None,
        description='An array of error details to accompany a problem details response.',
        max_length=1000,
    )


class AlreadyExists(ProblemDetails):
    type: Literal['https://problems-registry.smartbear.com/already-exists'] = Field(
        default='https://problems-registry.smartbear.com/already-exists',
        description='A URI reference that identifies the problem type.',
    )
    status: Literal[409] = Field(
        default=409,
        description='The HTTP status code generated by the origin server for this occurrence of the problem.',
    )
    title: Literal['Already exists'] = Field(
        default='Already exists',
        description='A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.',
    )
    detail: Literal['The resource being created already exists.'] = Field(
        default='The resource being created already exists.',
        description='A human-readable explanation specific to this occurrence of the problem.',
    )


class BadRequest(ProblemDetails):
    type: Literal['https://problems-registry.smartbear.com/bad-request'] = Field(
        default='https://problems-registry.smartbear.com/bad-request',
        description='A URI reference that identifies the problem type.',
    )
    status: Literal[400] = Field(
        default=400,
        description='The HTTP status code generated by the origin server for this occurrence of the problem.',
    )
    title: Literal['Bad Request'] = Field(
        default='Bad Request',
        description='A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.',
    )
    detail: Literal['The request is invalid or malformed.'] = Field(
        default='The request is invalid or malformed.',
        description='A human-readable explanation specific to this occurrence of the problem.',
    )


class BusinessRuleViolation(ProblemDetails):
    type: Literal[
        'https://problems-registry.smartbear.com/business-rule-violation'
    ] = Field(
        default='https://problems-registry.smartbear.com/business-rule-violation',
        description='A URI reference that identifies the problem type.',
    )
    status: Literal[422] = Field(
        default=422,
        description='The HTTP status code generated by the origin server for this occurrence of the problem.',
    )
    title: Literal['Business Rule Violation'] = Field(
        default='Business Rule Violation',
        description='A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.',
    )
    detail: Literal[
        'The request body is invalid and not meeting business rules.'
    ] = Field(
        default='The request body is invalid and not meeting business rules.',
        description='A human-readable explanation specific to this occurrence of the problem.',
    )


class Forbidden(ProblemDetails):
    type: Literal['https://problems-registry.smartbear.com/forbidden'] = Field(
        default='https://problems-registry.smartbear.com/forbidden',
        description='A URI reference that identifies the problem type.',
    )
    status: Literal[403] = Field(
        default=403,
        description='The HTTP status code generated by the origin server for this occurrence of the problem.',
    )
    title: Literal['Forbidden'] = Field(
        default='Forbidden',
        description='A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.',
    )
    detail: Literal[
        'The resource could not be returned as the requestor is not authorized.'
    ] = Field(
        default='The resource could not be returned as the requestor is not authorized.',
        description='A human-readable explanation specific to this occurrence of the problem.',
    )


class InvalidBodyPropertyFormat(ProblemDetails):
    type: Literal[
        'https://problems-registry.smartbear.com/invalid-body-property-format'
    ] = Field(
        default='https://problems-registry.smartbear.com/invalid-body-property-format',
        description='A URI reference that identifies the problem type.',
    )
    status: Literal[400] = Field(
        default=400,
        description='The HTTP status code generated by the origin server for this occurrence of the problem.',
    )
    title: Literal['Invalid Body Property Format'] = Field(
        default='Invalid Body Property Format',
        description='A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.',
    )
    detail: Literal['The request body contains a malformed property.'] = Field(
        default='The request body contains a malformed property.',
        description='A human-readable explanation specific to this occurrence of the problem.',
    )


class InvalidBodyPropertyValue(ProblemDetails):
    type: Literal[
        'https://problems-registry.smartbear.com/invalid-body-property-value'
    ] = Field(
        default='https://problems-registry.smartbear.com/invalid-body-property-value',
        description='A URI reference that identifies the problem type.',
    )
    status: Literal[400] = Field(
        default=400,
        description='The HTTP status code generated by the origin server for this occurrence of the problem.',
    )
    title: Literal['Invalid Body Property Value'] = Field(
        default='Invalid Body Property Value',
        description='A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.',
    )
    detail: Literal[
        'The request body contains an invalid body property value.'
    ] = Field(
        default='The request body contains an invalid body property value.',
        description='A human-readable explanation specific to this occurrence of the problem.',
    )


class InvalidParameters(ProblemDetails):
    type: Literal['https://problems-registry.smartbear.com/invalid-parameters'] = Field(
        default='https://problems-registry.smartbear.com/invalid-parameters',
        description='A URI reference that identifies the problem type.',
    )
    status: Literal[400] = Field(
        default=400,
        description='The HTTP status code generated by the origin server for this occurrence of the problem.',
    )
    title: Literal['Invalid parameters'] = Field(
        default='Invalid parameters',
        description='A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.',
    )
    detail: Literal[
        'The request contained invalid, or malformed parameters (path or header or query).'
    ] = Field(
        default='The request contained invalid, or malformed parameters (path or header or query).',
        description='A human-readable explanation specific to this occurrence of the problem.',
    )


class InvalidRequestHeaderFormat(ProblemDetails):
    type: Literal[
        'https://problems-registry.smartbear.com/invalid-request-header-format'
    ] = Field(
        default='https://problems-registry.smartbear.com/invalid-request-header-format',
        description='A URI reference that identifies the problem type.',
    )
    status: Literal[400] = Field(
        default=400,
        description='The HTTP status code generated by the origin server for this occurrence of the problem.',
    )
    title: Literal['Invalid Request Header Format'] = Field(
        default='Invalid Request Header Format',
        description='A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.',
    )
    detail: Literal[
        'The request contains a malformed request header parameter.'
    ] = Field(
        default='The request contains a malformed request header parameter.',
        description='A human-readable explanation specific to this occurrence of the problem.',
    )


class InvalidRequestParameterFormat(ProblemDetails):
    type: Literal[
        'https://problems-registry.smartbear.com/invalid-request-parameter-format'
    ] = Field(
        default='https://problems-registry.smartbear.com/invalid-request-parameter-format',
        description='A URI reference that identifies the problem type.',
    )
    status: Literal[400] = Field(
        default=400,
        description='The HTTP status code generated by the origin server for this occurrence of the problem.',
    )
    title: Literal['Invalid Request Parameter Format'] = Field(
        default='Invalid Request Parameter Format',
        description='A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.',
    )
    detail: Literal[
        'The request contains a malformed request query parameter.'
    ] = Field(
        default='The request contains a malformed request query parameter.',
        description='A human-readable explanation specific to this occurrence of the problem.',
    )


class InvalidRequestParameterValue(ProblemDetails):
    type: Literal[
        'https://problems-registry.smartbear.com/invalid-request-parameter-value'
    ] = Field(
        default='https://problems-registry.smartbear.com/invalid-request-parameter-value',
        description='A URI reference that identifies the problem type.',
    )
    status: Literal[400] = Field(
        default=400,
        description='The HTTP status code generated by the origin server for this occurrence of the problem.',
    )
    title: Literal['Invalid Request Parameter Value'] = Field(
        default='Invalid Request Parameter Value',
        description='A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.',
    )
    detail: Literal[
        'The request body contains an invalid request parameter value.'
    ] = Field(
        default='The request body contains an invalid request parameter value.',
        description='A human-readable explanation specific to this occurrence of the problem.',
    )


class LicenseCancelled(ProblemDetails):
    type: Literal['https://problems-registry.smartbear.com/license-cancelled'] = Field(
        default='https://problems-registry.smartbear.com/license-cancelled',
        description='A URI reference that identifies the problem type.',
    )
    status: Literal[503] = Field(
        default=503,
        description='The HTTP status code generated by the origin server for this occurrence of the problem.',
    )
    title: Literal['License Cancelled'] = Field(
        default='License Cancelled',
        description='A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.',
    )
    detail: Literal[
        'The service is unavailable as the license associated with your client or organization has been cancelled. Please contact your account manager or representative.'
    ] = Field(
        default='The service is unavailable as the license associated with your client or organization has been cancelled. Please contact your account manager or representative.',
        description='A human-readable explanation specific to this occurrence of the problem.',
    )


class LicenseExpired(ProblemDetails):
    type: Literal['https://problems-registry.smartbear.com/license-expired'] = Field(
        default='https://problems-registry.smartbear.com/license-expired',
        description='A URI reference that identifies the problem type.',
    )
    status: Literal[503] = Field(
        default=503,
        description='The HTTP status code generated by the origin server for this occurrence of the problem.',
    )
    title: Literal['License Expired'] = Field(
        default='License Expired',
        description='A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.',
    )
    detail: Literal[
        'The service is unavailable as the license associated with your client or organization has expired. Please contact your account manager or representative.'
    ] = Field(
        default='The service is unavailable as the license associated with your client or organization has expired. Please contact your account manager or representative.',
        description='A human-readable explanation specific to this occurrence of the problem.',
    )


class MissingBodyProperty(ProblemDetails):
    type: Literal[
        'https://problems-registry.smartbear.com/missing-body-property'
    ] = Field(
        default='https://problems-registry.smartbear.com/missing-body-property',
        description='A URI reference that identifies the problem type.',
    )
    status: Literal[400] = Field(
        default=400,
        description='The HTTP status code generated by the origin server for this occurrence of the problem.',
    )
    title: Literal['Missing body property'] = Field(
        default='Missing body property',
        description='A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.',
    )
    detail: Literal['The request is missing an expected body property.'] = Field(
        default='The request is missing an expected body property.',
        description='A human-readable explanation specific to this occurrence of the problem.',
    )


class MissingRequestHeader(ProblemDetails):
    type: Literal[
        'https://problems-registry.smartbear.com/missing-request-header'
    ] = Field(
        default='https://problems-registry.smartbear.com/missing-request-header',
        description='A URI reference that identifies the problem type.',
    )
    status: Literal[400] = Field(
        default=400,
        description='The HTTP status code generated by the origin server for this occurrence of the problem.',
    )
    title: Literal['Missing request header'] = Field(
        default='Missing request header',
        description='A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.',
    )
    detail: Literal['The request is missing an expected HTTP request header.'] = Field(
        default='The request is missing an expected HTTP request header.',
        description='A human-readable explanation specific to this occurrence of the problem.',
    )


class MissingRequestParameter(ProblemDetails):
    type: Literal[
        'https://problems-registry.smartbear.com/missing-request-parameter'
    ] = Field(
        default='https://problems-registry.smartbear.com/missing-request-parameter',
        description='A URI reference that identifies the problem type.',
    )
    status: Literal[400] = Field(
        default=400,
        description='The HTTP status code generated by the origin server for this occurrence of the problem.',
    )
    title: Literal['Missing request parameter'] = Field(
        default='Missing request parameter',
        description='A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.',
    )
    detail: Literal[
        'The request is missing an expected query or path parameter.'
    ] = Field(
        default='The request is missing an expected query or path parameter.',
        description='A human-readable explanation specific to this occurrence of the problem.',
    )


class NotFound(ProblemDetails):
    type: Literal['https://problems-registry.smartbear.com/not-found'] = Field(
        default='https://problems-registry.smartbear.com/not-found',
        description='A URI reference that identifies the problem type.',
    )
    status: Literal[404] = Field(
        default=404,
        description='The HTTP status code generated by the origin server for this occurrence of the problem.',
    )
    title: Literal['Not Found'] = Field(
        default='Not Found',
        description='A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.',
    )
    detail: Literal['The requested resource was not found.'] = Field(
        default='The requested resource was not found.',
        description='A human-readable explanation specific to this occurrence of the problem.',
    )


class ServerError(ProblemDetails):
    type: Literal['https://problems-registry.smartbear.com/server-error'] = Field(
        default='https://problems-registry.smartbear.com/server-error',
        description='A URI reference that identifies the problem type.',
    )
    status: Literal[500] = Field(
        default=500,
        description='The HTTP status code generated by the origin server for this occurrence of the problem.',
    )
    title: Literal['Server Error'] = Field(
        default='Server Error',
        description='A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.',
    )
    detail: Literal['The server encountered an unexpected error.'] = Field(
        default='The server encountered an unexpected error.',
        description='A human-readable explanation specific to this occurrence of the problem.',
    )


class ServiceUnavailable(ProblemDetails):
    type: Literal[
        'https://problems-registry.smartbear.com/service-unavailable'
    ] = Field(
        default='https://problems-registry.smartbear.com/service-unavailable',
        description='A URI reference that identifies the problem type.',
    )
    status: Literal[503] = Field(
        default=503,
        description='The HTTP status code generated by the origin server for this occurrence of the problem.',
    )
    title: Literal['Service Unavailable'] = Field(
        default='Service Unavailable',
        description='A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.',
    )
    detail: Literal['The service is currently unavailable.'] = Field(
        'The service is currently unavailable.',
        description='A human-readable explanation specific to this occurrence of the problem.',
    )


class Unauthorized(ProblemDetails):
    type: Literal['https://problems-registry.smartbear.com/unauthorized'] = Field(
        default='https://problems-registry.smartbear.com/unauthorized',
        description='A URI reference that identifies the problem type.',
    )
    status: Literal[401] = Field(
        default=401,
        description='The HTTP status code generated by the origin server for this occurrence of the problem.',
    )
    title: Literal['Unauthorized'] = Field(
        default='Unauthorized',
        description='A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.',
    )
    detail: Literal[
        'Access token not set or invalid, and the requested resource could not be returned.'
    ] = Field(
        default='Access token not set or invalid, and the requested resource could not be returned.',
        description='A human-readable explanation specific to this occurrence of the problem.',
    )


class ValidationError(ProblemDetails):
    type: Literal['https://problems-registry.smartbear.com/validation-error'] = Field(
        default='https://problems-registry.smartbear.com/validation-error',
        description='A URI reference that identifies the problem type.',
    )
    status: Literal[422] = Field(
        default=422,
        description='The HTTP status code generated by the origin server for this occurrence of the problem.',
    )
    title: Literal['Validation Error'] = Field(
        default='Validation Error',
        description='A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.',
    )
    detail: Literal['The request is not valid.'] = Field(
        default='The request is not valid.',
        description='A human-readable explanation specific to this occurrence of the problem.',
    )
