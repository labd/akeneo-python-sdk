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
from openapi_client.models.attribute_options_embedded_items_inner_all_of_labels import AttributeOptionsEmbeddedItemsInnerAllOfLabels

class PatchAttributesAttributeCodeOptionsRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    code: StrictStr = Field(..., description="Code of option")
    attribute: Optional[StrictStr] = Field(None, description="Code of attribute related to the attribute option")
    sort_order: Optional[StrictInt] = Field(None, description="Order of attribute option")
    labels: Optional[AttributeOptionsEmbeddedItemsInnerAllOfLabels] = None
    __properties = ["code", "attribute", "sort_order", "labels"]

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
    def from_json(cls, json_str: str) -> PatchAttributesAttributeCodeOptionsRequest:
        """Create an instance of PatchAttributesAttributeCodeOptionsRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of labels
        if self.labels:
            _dict['labels'] = self.labels.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PatchAttributesAttributeCodeOptionsRequest:
        """Create an instance of PatchAttributesAttributeCodeOptionsRequest from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return PatchAttributesAttributeCodeOptionsRequest.parse_obj(obj)

        _obj = PatchAttributesAttributeCodeOptionsRequest.parse_obj({
            "code": obj.get("code"),
            "attribute": obj.get("attribute"),
            "sort_order": obj.get("sort_order"),
            "labels": AttributeOptionsEmbeddedItemsInnerAllOfLabels.from_dict(obj.get("labels")) if obj.get("labels") is not None else None
        })
        return _obj

