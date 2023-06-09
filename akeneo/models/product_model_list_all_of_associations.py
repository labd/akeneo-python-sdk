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


from typing import Dict, Optional
from pydantic import BaseModel, Field
from akeneo.models.product_list_all_of1_associations_association_type_code import ProductListAllOf1AssociationsAssociationTypeCode

class ProductModelListAllOfAssociations(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    association_type_code: Optional[Dict[str, ProductListAllOf1AssociationsAssociationTypeCode]] = Field(None, alias="associationTypeCode")
    __properties = ["associationTypeCode"]

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
    def from_json(cls, json_str: str) -> ProductModelListAllOfAssociations:
        """Create an instance of ProductModelListAllOfAssociations from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in association_type_code (dict)
        _field_dict = {}
        if self.association_type_code:
            for _key in self.association_type_code:
                if self.association_type_code[_key]:
                    _field_dict[_key] = self.association_type_code[_key].to_dict()
            _dict['associationTypeCode'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProductModelListAllOfAssociations:
        """Create an instance of ProductModelListAllOfAssociations from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ProductModelListAllOfAssociations.parse_obj(obj)

        _obj = ProductModelListAllOfAssociations.parse_obj({
            "association_type_code": dict((_k, Dict[str, ProductListAllOf1AssociationsAssociationTypeCode].from_dict(_v)) for _k, _v in obj.get("associationTypeCode").items())
        })
        return _obj

