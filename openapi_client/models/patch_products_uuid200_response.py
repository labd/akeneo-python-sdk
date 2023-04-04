# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr

class PatchProductsUuid200Response(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    line: Optional[StrictInt] = Field(None, description="Line number")
    uuid: Optional[StrictStr] = Field(None, description="Product uuid")
    status_code: Optional[StrictInt] = Field(None, description="HTTP status code, see <a href=\"/documentation/responses.html#client-errors\">Client errors</a> to understand the meaning of each code")
    message: Optional[StrictStr] = Field(None, description="Message explaining the error")
    __properties = ["line", "uuid", "status_code", "message"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> PatchProductsUuid200Response:
        """Create an instance of PatchProductsUuid200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PatchProductsUuid200Response:
        """Create an instance of PatchProductsUuid200Response from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return PatchProductsUuid200Response.parse_obj(obj)

        _obj = PatchProductsUuid200Response.parse_obj({
            "line": obj.get("line"),
            "uuid": obj.get("uuid"),
            "status_code": obj.get("status_code"),
            "message": obj.get("message")
        })
        return _obj

