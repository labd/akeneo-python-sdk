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
from pydantic import BaseModel, Field, StrictStr

class PatchMeasurementFamilies200ResponseInnerErrorsInner(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    var_property: Optional[StrictStr] = Field(None, alias="property")
    message: Optional[StrictStr] = None
    __properties = ["property", "message"]

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
    def from_json(cls, json_str: str) -> PatchMeasurementFamilies200ResponseInnerErrorsInner:
        """Create an instance of PatchMeasurementFamilies200ResponseInnerErrorsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PatchMeasurementFamilies200ResponseInnerErrorsInner:
        """Create an instance of PatchMeasurementFamilies200ResponseInnerErrorsInner from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return PatchMeasurementFamilies200ResponseInnerErrorsInner.parse_obj(obj)

        _obj = PatchMeasurementFamilies200ResponseInnerErrorsInner.parse_obj({
            "var_property": obj.get("property"),
            "message": obj.get("message")
        })
        return _obj

