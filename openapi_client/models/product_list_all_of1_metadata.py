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
from pydantic import BaseModel, Field, StrictStr, validator

class ProductListAllOf1Metadata(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    workflow_status: Optional[StrictStr] = Field(None, description="Status of the product regarding the user permissions")
    __properties = ["workflow_status"]

    @validator('workflow_status')
    def workflow_status_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('read_only', 'draft_in_progress', 'proposal_waiting_for_approval', 'working_copy'):
            raise ValueError("must validate the enum values ('read_only', 'draft_in_progress', 'proposal_waiting_for_approval', 'working_copy')")
        return v

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
    def from_json(cls, json_str: str) -> ProductListAllOf1Metadata:
        """Create an instance of ProductListAllOf1Metadata from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProductListAllOf1Metadata:
        """Create an instance of ProductListAllOf1Metadata from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ProductListAllOf1Metadata.parse_obj(obj)

        _obj = ProductListAllOf1Metadata.parse_obj({
            "workflow_status": obj.get("workflow_status")
        })
        return _obj

