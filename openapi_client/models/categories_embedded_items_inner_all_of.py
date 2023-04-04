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
from openapi_client.models.categories_embedded_items_inner_all_of_labels import CategoriesEmbeddedItemsInnerAllOfLabels
from openapi_client.models.categories_embedded_items_inner_all_of_values import CategoriesEmbeddedItemsInnerAllOfValues

class CategoriesEmbeddedItemsInnerAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    code: StrictStr = Field(..., description="Category code")
    parent: Optional[StrictStr] = Field('null', description="Category code of the parent's category")
    updated: Optional[StrictStr] = Field(None, description="Date of the last update")
    position: Optional[StrictInt] = Field(None, description="Position of the category in its level, start from 1 (only available since the 7.0 version and when query parameter \"with_position\" is set to \"true\")")
    labels: Optional[CategoriesEmbeddedItemsInnerAllOfLabels] = None
    values: Optional[CategoriesEmbeddedItemsInnerAllOfValues] = None
    __properties = ["code", "parent", "updated", "position", "labels", "values"]

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
    def from_json(cls, json_str: str) -> CategoriesEmbeddedItemsInnerAllOf:
        """Create an instance of CategoriesEmbeddedItemsInnerAllOf from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of values
        if self.values:
            _dict['values'] = self.values.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CategoriesEmbeddedItemsInnerAllOf:
        """Create an instance of CategoriesEmbeddedItemsInnerAllOf from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return CategoriesEmbeddedItemsInnerAllOf.parse_obj(obj)

        _obj = CategoriesEmbeddedItemsInnerAllOf.parse_obj({
            "code": obj.get("code"),
            "parent": obj.get("parent") if obj.get("parent") is not None else 'null',
            "updated": obj.get("updated"),
            "position": obj.get("position"),
            "labels": CategoriesEmbeddedItemsInnerAllOfLabels.from_dict(obj.get("labels")) if obj.get("labels") is not None else None,
            "values": CategoriesEmbeddedItemsInnerAllOfValues.from_dict(obj.get("values")) if obj.get("values") is not None else None
        })
        return _obj

