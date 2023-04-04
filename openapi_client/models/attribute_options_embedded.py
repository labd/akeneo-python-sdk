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
from pydantic import BaseModel
from openapi_client.models.attribute_options_embedded_items_inner import AttributeOptionsEmbeddedItemsInner

class AttributeOptionsEmbedded(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    items: Optional[List[AttributeOptionsEmbeddedItemsInner]] = None
    __properties = ["items"]

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
    def from_json(cls, json_str: str) -> AttributeOptionsEmbedded:
        """Create an instance of AttributeOptionsEmbedded from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AttributeOptionsEmbedded:
        """Create an instance of AttributeOptionsEmbedded from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return AttributeOptionsEmbedded.parse_obj(obj)

        _obj = AttributeOptionsEmbedded.parse_obj({
            "items": [AttributeOptionsEmbeddedItemsInner.from_dict(_item) for _item in obj.get("items")] if obj.get("items") is not None else None
        })
        return _obj

