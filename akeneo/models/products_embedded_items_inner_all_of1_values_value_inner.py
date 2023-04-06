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
from akeneo.models.products_embedded_items_inner_all_of1_values_value_inner_linked_data import ProductsEmbeddedItemsInnerAllOf1ValuesValueInnerLinkedData

class ProductsEmbeddedItemsInnerAllOf1ValuesValueInner(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    scope: Optional[StrictStr] = Field(None, description="<a href='api-reference.html#Channel'>Channel</a> code of the product value")
    locale: Optional[StrictStr] = Field(None, description="<a href='api-reference.html#Locale'>Locale</a> code of the product value")
    data: Optional[Any] = Field(None, description="Product value. See <a href='/concepts/products.html#the-data-format'>the `data` format</a> section for more details.")
    linked_data: Optional[ProductsEmbeddedItemsInnerAllOf1ValuesValueInnerLinkedData] = None
    __properties = ["scope", "locale", "data", "linked_data"]

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
    def from_json(cls, json_str: str) -> ProductsEmbeddedItemsInnerAllOf1ValuesValueInner:
        """Create an instance of ProductsEmbeddedItemsInnerAllOf1ValuesValueInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of linked_data
        if self.linked_data:
            _dict['linked_data'] = self.linked_data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProductsEmbeddedItemsInnerAllOf1ValuesValueInner:
        """Create an instance of ProductsEmbeddedItemsInnerAllOf1ValuesValueInner from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ProductsEmbeddedItemsInnerAllOf1ValuesValueInner.parse_obj(obj)

        _obj = ProductsEmbeddedItemsInnerAllOf1ValuesValueInner.parse_obj({
            "scope": obj.get("scope"),
            "locale": obj.get("locale"),
            "data": obj.get("data"),
            "linked_data": ProductsEmbeddedItemsInnerAllOf1ValuesValueInnerLinkedData.from_dict(obj.get("linked_data")) if obj.get("linked_data") is not None else None
        })
        return _obj

