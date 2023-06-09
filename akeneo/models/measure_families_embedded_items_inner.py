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
from pydantic import BaseModel, Field, StrictStr
from akeneo.models.measure_families_embedded_items_inner_all_of_units_inner import MeasureFamiliesEmbeddedItemsInnerAllOfUnitsInner
from akeneo.models.products_embedded_items_inner_all_of_links import ProductsEmbeddedItemsInnerAllOfLinks

class MeasureFamiliesEmbeddedItemsInner(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    links: Optional[ProductsEmbeddedItemsInnerAllOfLinks] = Field(None, alias="_links")
    code: StrictStr = Field(..., description="Measure family code")
    standard: Optional[StrictStr] = Field(None, description="Measure family standard")
    units: Optional[List[MeasureFamiliesEmbeddedItemsInnerAllOfUnitsInner]] = Field(None, description="Family units")
    __properties = ["_links", "code", "standard", "units"]

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
    def from_json(cls, json_str: str) -> MeasureFamiliesEmbeddedItemsInner:
        """Create an instance of MeasureFamiliesEmbeddedItemsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in units (list)
        _items = []
        if self.units:
            for _item in self.units:
                if _item:
                    _items.append(_item.to_dict())
            _dict['units'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MeasureFamiliesEmbeddedItemsInner:
        """Create an instance of MeasureFamiliesEmbeddedItemsInner from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return MeasureFamiliesEmbeddedItemsInner.parse_obj(obj)

        _obj = MeasureFamiliesEmbeddedItemsInner.parse_obj({
            "links": ProductsEmbeddedItemsInnerAllOfLinks.from_dict(obj.get("_links")) if obj.get("_links") is not None else None,
            "code": obj.get("code"),
            "standard": obj.get("standard"),
            "units": [MeasureFamiliesEmbeddedItemsInnerAllOfUnitsInner.from_dict(_item) for _item in obj.get("units")] if obj.get("units") is not None else None
        })
        return _obj

