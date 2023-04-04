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
from pydantic import BaseModel, Field, StrictBool, StrictStr

class PostAppCatalog201Response(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[StrictStr] = Field(None, description="Catalog id")
    name: Optional[StrictStr] = Field(None, description="Catalog name")
    enabled: Optional[StrictBool] = Field(False, description="Whether the catalog is enabled or not")
    __properties = ["id", "name", "enabled"]

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
    def from_json(cls, json_str: str) -> PostAppCatalog201Response:
        """Create an instance of PostAppCatalog201Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PostAppCatalog201Response:
        """Create an instance of PostAppCatalog201Response from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return PostAppCatalog201Response.parse_obj(obj)

        _obj = PostAppCatalog201Response.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "enabled": obj.get("enabled") if obj.get("enabled") is not None else False
        })
        return _obj

