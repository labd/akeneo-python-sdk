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
from pydantic import BaseModel, Field
from openapi_client.models.product_model_list_all_of_quantified_associations_quantified_association_type_code import ProductModelListAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode

class ProductModelListAllOfQuantifiedAssociations(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    quantified_association_type_code: Optional[ProductModelListAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode] = Field(None, alias="quantifiedAssociationTypeCode")
    __properties = ["quantifiedAssociationTypeCode"]

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
    def from_json(cls, json_str: str) -> ProductModelListAllOfQuantifiedAssociations:
        """Create an instance of ProductModelListAllOfQuantifiedAssociations from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of quantified_association_type_code
        if self.quantified_association_type_code:
            _dict['quantifiedAssociationTypeCode'] = self.quantified_association_type_code.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProductModelListAllOfQuantifiedAssociations:
        """Create an instance of ProductModelListAllOfQuantifiedAssociations from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ProductModelListAllOfQuantifiedAssociations.parse_obj(obj)

        _obj = ProductModelListAllOfQuantifiedAssociations.parse_obj({
            "quantified_association_type_code": ProductModelListAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode.from_dict(obj.get("quantifiedAssociationTypeCode")) if obj.get("quantifiedAssociationTypeCode") is not None else None
        })
        return _obj

