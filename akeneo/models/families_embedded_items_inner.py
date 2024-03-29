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
from akeneo.models.families_embedded_items_inner_all_of_attribute_requirements import FamiliesEmbeddedItemsInnerAllOfAttributeRequirements
from akeneo.models.families_embedded_items_inner_all_of_labels import FamiliesEmbeddedItemsInnerAllOfLabels
from akeneo.models.products_embedded_items_inner_all_of_links import ProductsEmbeddedItemsInnerAllOfLinks

class FamiliesEmbeddedItemsInner(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    links: Optional[ProductsEmbeddedItemsInnerAllOfLinks] = Field(None, alias="_links")
    code: StrictStr = Field(..., description="Family code")
    attribute_as_label: StrictStr = Field(..., description="Attribute code used as label")
    attribute_as_image: Optional[StrictStr] = Field('null', description="Attribute code used as the main picture in the user interface (only since v2.0)")
    attributes: Optional[List[StrictStr]] = Field(None, description="Attributes codes that compose the family")
    attribute_requirements: Optional[FamiliesEmbeddedItemsInnerAllOfAttributeRequirements] = None
    labels: Optional[Dict[str, StrictStr]] = Field(None, description="Family variant labels for each locale")
    __properties = ["_links", "code", "attribute_as_label", "attribute_as_image", "attributes", "attribute_requirements", "labels"]

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
    def from_json(cls, json_str: str) -> FamiliesEmbeddedItemsInner:
        """Create an instance of FamiliesEmbeddedItemsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of attribute_requirements
        if self.attribute_requirements:
            _dict['attribute_requirements'] = self.attribute_requirements.to_dict()
        # override the default output from pydantic by calling `to_dict()` of labels
        if self.labels:
            _dict['labels'] = self.labels.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FamiliesEmbeddedItemsInner:
        """Create an instance of FamiliesEmbeddedItemsInner from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return FamiliesEmbeddedItemsInner.parse_obj(obj)

        _obj = FamiliesEmbeddedItemsInner.parse_obj({
            "links": ProductsEmbeddedItemsInnerAllOfLinks.from_dict(obj.get("_links")) if obj.get("_links") is not None else None,
            "code": obj.get("code"),
            "attribute_as_label": obj.get("attribute_as_label"),
            "attribute_as_image": obj.get("attribute_as_image") if obj.get("attribute_as_image") is not None else 'null',
            "attributes": obj.get("attributes"),
            "attribute_requirements": FamiliesEmbeddedItemsInnerAllOfAttributeRequirements.from_dict(obj.get("attribute_requirements")) if obj.get("attribute_requirements") is not None else None,
            "labels": obj.get("labels") if obj.get("labels") is not None else None
        })
        return _obj

