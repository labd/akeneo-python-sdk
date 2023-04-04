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
from openapi_client.models.channels_embedded_items_inner_all_of_conversion_units import ChannelsEmbeddedItemsInnerAllOfConversionUnits
from openapi_client.models.channels_embedded_items_inner_all_of_labels import ChannelsEmbeddedItemsInnerAllOfLabels
from openapi_client.models.products_embedded_items_inner_all_of_links import ProductsEmbeddedItemsInnerAllOfLinks

class ChannelsEmbeddedItemsInner(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    links: Optional[ProductsEmbeddedItemsInnerAllOfLinks] = Field(None, alias="_links")
    code: StrictStr = Field(..., description="Channel code")
    locales: List[StrictStr] = Field(..., description="Codes of activated locales for the channel")
    currencies: List[StrictStr] = Field(..., description="Codes of activated currencies for the channel")
    category_tree: StrictStr = Field(..., description="Code of the category tree linked to the channel")
    conversion_units: Optional[ChannelsEmbeddedItemsInnerAllOfConversionUnits] = None
    labels: Optional[ChannelsEmbeddedItemsInnerAllOfLabels] = None
    __properties = ["_links", "code", "locales", "currencies", "category_tree", "conversion_units", "labels"]

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
    def from_json(cls, json_str: str) -> ChannelsEmbeddedItemsInner:
        """Create an instance of ChannelsEmbeddedItemsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of conversion_units
        if self.conversion_units:
            _dict['conversion_units'] = self.conversion_units.to_dict()
        # override the default output from pydantic by calling `to_dict()` of labels
        if self.labels:
            _dict['labels'] = self.labels.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ChannelsEmbeddedItemsInner:
        """Create an instance of ChannelsEmbeddedItemsInner from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ChannelsEmbeddedItemsInner.parse_obj(obj)

        _obj = ChannelsEmbeddedItemsInner.parse_obj({
            "links": ProductsEmbeddedItemsInnerAllOfLinks.from_dict(obj.get("_links")) if obj.get("_links") is not None else None,
            "code": obj.get("code"),
            "locales": obj.get("locales"),
            "currencies": obj.get("currencies"),
            "category_tree": obj.get("category_tree"),
            "conversion_units": ChannelsEmbeddedItemsInnerAllOfConversionUnits.from_dict(obj.get("conversion_units")) if obj.get("conversion_units") is not None else None,
            "labels": ChannelsEmbeddedItemsInnerAllOfLabels.from_dict(obj.get("labels")) if obj.get("labels") is not None else None
        })
        return _obj

