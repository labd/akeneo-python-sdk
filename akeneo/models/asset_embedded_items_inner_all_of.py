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


from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr
from akeneo.models.asset_embedded_items_inner_all_of_values_value_inner import AssetEmbeddedItemsInnerAllOfValuesValueInner

class AssetEmbeddedItemsInnerAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    code: StrictStr = Field(..., description="Code of the asset")
    values: Optional[Dict[str, List[AssetEmbeddedItemsInnerAllOfValuesValueInner]]] = Field(None, description="Asset attributes values, see the <a href='/concepts/asset-manager.html#focus-on-the-asset-values'>Focus on the asset values</a> section for more details.")
    created: Optional[StrictStr] = Field(None, description="Date of creation")
    updated: Optional[StrictStr] = Field(None, description="Date of the last update")
    __properties = ["code", "values", "created", "updated"]

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
    def from_json(cls, json_str: str) -> AssetEmbeddedItemsInnerAllOf:
        """Create an instance of AssetEmbeddedItemsInnerAllOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in values (dict)
        _field_dict = {}
        if self.values:
            for _key in self.values:
                if self.values[_key]:
                    _field_dict[_key] = self.values[_key].to_dict()
            _dict['values'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AssetEmbeddedItemsInnerAllOf:
        """Create an instance of AssetEmbeddedItemsInnerAllOf from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return AssetEmbeddedItemsInnerAllOf.parse_obj(obj)

        _obj = AssetEmbeddedItemsInnerAllOf.parse_obj({
            "code": obj.get("code"),
            "values": dict((_k, [AssetEmbeddedItemsInnerAllOfValuesValueInner.from_dict(_item) for _item in _v]) for _k, _v in obj.get("values").items()), 
            "created": obj.get("created"),
            "updated": obj.get("updated")
        })
        return _obj

