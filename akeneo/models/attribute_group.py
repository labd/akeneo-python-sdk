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
from pydantic import BaseModel, Field, StrictInt, StrictStr
from akeneo.models.attribute_groups_embedded_items_inner_all_of_labels import AttributeGroupsEmbeddedItemsInnerAllOfLabels

class AttributeGroup(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    code: StrictStr = Field(..., description="Attribute group code")
    sort_order: Optional[StrictInt] = Field(None, description="Attribute group order among other attribute groups")
    attributes: Optional[List[StrictStr]] = Field(None, description="Attribute codes that compose the attribute group")
    labels: Optional[Dict[str, StrictStr]] = Field(None, description="Attribute group labels for each locale")
    __properties = ["code", "sort_order", "attributes", "labels"]

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
    def from_json(cls, json_str: str) -> AttributeGroup:
        """Create an instance of AttributeGroup from a JSON string"""
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
    def from_dict(cls, obj: dict) -> AttributeGroup:
        """Create an instance of AttributeGroup from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return AttributeGroup.parse_obj(obj)

        _obj = AttributeGroup.parse_obj({
            "code": obj.get("code"),
            "sort_order": obj.get("sort_order"),
            "attributes": obj.get("attributes"),
            "labels": obj.get("labels"),
        })
        return _obj

