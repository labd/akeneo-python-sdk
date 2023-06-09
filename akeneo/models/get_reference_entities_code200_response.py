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
from pydantic import BaseModel, Field, StrictStr
from akeneo.models.get_reference_entities_code200_response_links import GetReferenceEntitiesCode200ResponseLinks
from akeneo.models.reference_entities_embedded_items_inner_all_of1_labels import ReferenceEntitiesEmbeddedItemsInnerAllOf1Labels

class GetReferenceEntitiesCode200Response(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    links: Optional[GetReferenceEntitiesCode200ResponseLinks] = Field(None, alias="_links")
    code: StrictStr = Field(..., description="Reference entity code")
    image: Optional[StrictStr] = Field('null', description="Code of the reference entity image")
    labels: Optional[ReferenceEntitiesEmbeddedItemsInnerAllOf1Labels] = None
    __properties = ["_links", "code", "image", "labels"]

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
    def from_json(cls, json_str: str) -> GetReferenceEntitiesCode200Response:
        """Create an instance of GetReferenceEntitiesCode200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of labels
        if self.labels:
            _dict['labels'] = self.labels.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetReferenceEntitiesCode200Response:
        """Create an instance of GetReferenceEntitiesCode200Response from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return GetReferenceEntitiesCode200Response.parse_obj(obj)

        _obj = GetReferenceEntitiesCode200Response.parse_obj({
            "links": GetReferenceEntitiesCode200ResponseLinks.from_dict(obj.get("_links")) if obj.get("_links") is not None else None,
            "code": obj.get("code"),
            "image": obj.get("image") if obj.get("image") is not None else 'null',
            "labels": ReferenceEntitiesEmbeddedItemsInnerAllOf1Labels.from_dict(obj.get("labels")) if obj.get("labels") is not None else None
        })
        return _obj

