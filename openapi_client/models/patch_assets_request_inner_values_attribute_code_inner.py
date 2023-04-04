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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr

class PatchAssetsRequestInnerValuesAttributeCodeInner(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    channel: Optional[StrictStr] = Field(None, description="Channel code of the asset attribute value")
    locale: Optional[StrictStr] = Field(None, description="Locale code of the asset attribute value")
    data: Optional[Dict[str, Any]] = Field(None, description="Asset attribute value. See <a href='/concepts/asset-manager.html#the-data-format'>the `data` format</a> section for more details.")
    __properties = ["channel", "locale", "data"]

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
    def from_json(cls, json_str: str) -> PatchAssetsRequestInnerValuesAttributeCodeInner:
        """Create an instance of PatchAssetsRequestInnerValuesAttributeCodeInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PatchAssetsRequestInnerValuesAttributeCodeInner:
        """Create an instance of PatchAssetsRequestInnerValuesAttributeCodeInner from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return PatchAssetsRequestInnerValuesAttributeCodeInner.parse_obj(obj)

        _obj = PatchAssetsRequestInnerValuesAttributeCodeInner.parse_obj({
            "channel": obj.get("channel"),
            "locale": obj.get("locale"),
            "data": obj.get("data")
        })
        return _obj

