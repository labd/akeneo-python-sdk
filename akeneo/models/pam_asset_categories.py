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
from pydantic import BaseModel, Field, StrictInt
from akeneo.models.pam_asset_categories_embedded import PAMAssetCategoriesEmbedded
from akeneo.models.products_links import ProductsLinks

class PAMAssetCategories(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    embedded: Optional[PAMAssetCategoriesEmbedded] = Field(None, alias="_embedded")
    links: Optional[ProductsLinks] = Field(None, alias="_links")
    current_page: Optional[StrictInt] = Field(None, description="Current page number")
    __properties = ["_embedded", "_links", "current_page"]

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
    def from_json(cls, json_str: str) -> PAMAssetCategories:
        """Create an instance of PAMAssetCategories from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of embedded
        if self.embedded:
            _dict['_embedded'] = self.embedded.to_dict()
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PAMAssetCategories:
        """Create an instance of PAMAssetCategories from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return PAMAssetCategories.parse_obj(obj)

        _obj = PAMAssetCategories.parse_obj({
            "embedded": PAMAssetCategoriesEmbedded.from_dict(obj.get("_embedded")) if obj.get("_embedded") is not None else None,
            "links": ProductsLinks.from_dict(obj.get("_links")) if obj.get("_links") is not None else None,
            "current_page": obj.get("current_page")
        })
        return _obj

