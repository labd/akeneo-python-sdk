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
from pydantic import BaseModel, Field
from openapi_client.models.products_embedded_items_inner_all_of1_quantified_associations_quantified_association_type_code_product_models_inner import ProductsEmbeddedItemsInnerAllOf1QuantifiedAssociationsQuantifiedAssociationTypeCodeProductModelsInner
from openapi_client.models.products_embedded_items_inner_all_of1_quantified_associations_quantified_association_type_code_products_inner import ProductsEmbeddedItemsInnerAllOf1QuantifiedAssociationsQuantifiedAssociationTypeCodeProductsInner

class ProductModelsEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    products: Optional[List[ProductsEmbeddedItemsInnerAllOf1QuantifiedAssociationsQuantifiedAssociationTypeCodeProductsInner]] = Field(None, description="Array of objects containing product identifiers and quantities with which the product model is in relation")
    product_models: Optional[List[ProductsEmbeddedItemsInnerAllOf1QuantifiedAssociationsQuantifiedAssociationTypeCodeProductModelsInner]] = Field(None, description="Array of objects containing product model codes and quantities with which the product model is in relation")
    __properties = ["products", "product_models"]

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
    def from_json(cls, json_str: str) -> ProductModelsEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode:
        """Create an instance of ProductModelsEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in products (list)
        _items = []
        if self.products:
            for _item in self.products:
                if _item:
                    _items.append(_item.to_dict())
            _dict['products'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in product_models (list)
        _items = []
        if self.product_models:
            for _item in self.product_models:
                if _item:
                    _items.append(_item.to_dict())
            _dict['product_models'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProductModelsEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode:
        """Create an instance of ProductModelsEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ProductModelsEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode.parse_obj(obj)

        _obj = ProductModelsEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode.parse_obj({
            "products": [ProductsEmbeddedItemsInnerAllOf1QuantifiedAssociationsQuantifiedAssociationTypeCodeProductsInner.from_dict(_item) for _item in obj.get("products")] if obj.get("products") is not None else None,
            "product_models": [ProductsEmbeddedItemsInnerAllOf1QuantifiedAssociationsQuantifiedAssociationTypeCodeProductModelsInner.from_dict(_item) for _item in obj.get("product_models")] if obj.get("product_models") is not None else None
        })
        return _obj

