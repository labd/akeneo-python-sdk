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


from typing import List, Optional
from pydantic import BaseModel, Field
from openapi_client.models.patch_reference_entity_records_request_inner_values_attribute_code_inner import PatchReferenceEntityRecordsRequestInnerValuesAttributeCodeInner

class PatchReferenceEntityRecordsRequestInnerValues(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    attribute_code: Optional[List[PatchReferenceEntityRecordsRequestInnerValuesAttributeCodeInner]] = Field(None, alias="attributeCode")
    __properties = ["attributeCode"]

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
    def from_json(cls, json_str: str) -> PatchReferenceEntityRecordsRequestInnerValues:
        """Create an instance of PatchReferenceEntityRecordsRequestInnerValues from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in attribute_code (list)
        _items = []
        if self.attribute_code:
            for _item in self.attribute_code:
                if _item:
                    _items.append(_item.to_dict())
            _dict['attributeCode'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PatchReferenceEntityRecordsRequestInnerValues:
        """Create an instance of PatchReferenceEntityRecordsRequestInnerValues from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return PatchReferenceEntityRecordsRequestInnerValues.parse_obj(obj)

        _obj = PatchReferenceEntityRecordsRequestInnerValues.parse_obj({
            "attribute_code": [PatchReferenceEntityRecordsRequestInnerValuesAttributeCodeInner.from_dict(_item) for _item in obj.get("attributeCode")] if obj.get("attributeCode") is not None else None
        })
        return _obj

