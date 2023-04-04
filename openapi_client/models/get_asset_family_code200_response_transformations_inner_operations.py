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
from pydantic import BaseModel, StrictStr
from openapi_client.models.get_asset_family_code200_response_transformations_inner_operations_parameters import GetAssetFamilyCode200ResponseTransformationsInnerOperationsParameters

class GetAssetFamilyCode200ResponseTransformationsInnerOperations(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    type: Optional[StrictStr] = None
    parameters: Optional[GetAssetFamilyCode200ResponseTransformationsInnerOperationsParameters] = None
    __properties = ["type", "parameters"]

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
    def from_json(cls, json_str: str) -> GetAssetFamilyCode200ResponseTransformationsInnerOperations:
        """Create an instance of GetAssetFamilyCode200ResponseTransformationsInnerOperations from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of parameters
        if self.parameters:
            _dict['parameters'] = self.parameters.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetAssetFamilyCode200ResponseTransformationsInnerOperations:
        """Create an instance of GetAssetFamilyCode200ResponseTransformationsInnerOperations from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return GetAssetFamilyCode200ResponseTransformationsInnerOperations.parse_obj(obj)

        _obj = GetAssetFamilyCode200ResponseTransformationsInnerOperations.parse_obj({
            "type": obj.get("type"),
            "parameters": GetAssetFamilyCode200ResponseTransformationsInnerOperationsParameters.from_dict(obj.get("parameters")) if obj.get("parameters") is not None else None
        })
        return _obj

