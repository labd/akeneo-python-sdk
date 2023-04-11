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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr
from akeneo.models.post_products_request_associations import PostProductsRequestAssociations
from akeneo.models.products_embedded_items_inner_all_of1_completenesses_inner import ProductsEmbeddedItemsInnerAllOf1CompletenessesInner
from akeneo.models.products_embedded_items_inner_all_of1_metadata import ProductsEmbeddedItemsInnerAllOf1Metadata
from akeneo.models.products_embedded_items_inner_all_of1_quantified_associations import ProductsEmbeddedItemsInnerAllOf1QuantifiedAssociations
from akeneo.models.products_embedded_items_inner_all_of1_values_value_inner import ProductsEmbeddedItemsInnerAllOf1ValuesValueInner

class Product(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    uuid: Optional[StrictStr] = Field(None, description="Product UUID")
    identifier: StrictStr = Field(..., description="Product identifier, i.e. the value of the only `pim_catalog_identifier` attribute")
    enabled: Optional[StrictBool] = Field(True, description="Whether the product is enabled")
    family: Optional[StrictStr] = Field('null only in the case of a non variant product', description="<a href='api-reference.html#Family'>Family</a> code from which the product inherits its attributes and attributes requirements.")
    categories: Optional[List[StrictStr]] = Field(None, description="Codes of the <a href='api-reference.html#Category'>categories</a> in which the product is classified")
    groups: Optional[List[StrictStr]] = Field(None, description="Codes of the groups to which the product belong")
    parent: Optional[StrictStr] = Field('null', description="Code of the parent <a href='api-reference.html#Productmodel'>product model</a> when the product is a variant (only available since the 2.0). This parent can be modified since the 2.3.")
    values: Optional[Dict[str, List[ProductsEmbeddedItemsInnerAllOf1ValuesValueInner]]] = Field(None, description="Product attributes values, see <a href='/concepts/products.html#focus-on-the-product-values'>Product values</a> section for more details")
    associations: Optional[PostProductsRequestAssociations] = None
    quantified_associations: Optional[ProductsEmbeddedItemsInnerAllOf1QuantifiedAssociations] = None
    created: Optional[StrictStr] = Field(None, description="Date of creation")
    updated: Optional[StrictStr] = Field(None, description="Date of the last update")
    metadata: Optional[ProductsEmbeddedItemsInnerAllOf1Metadata] = None
    quality_scores: Optional[Dict[str, Any]] = Field(None, description="Product quality scores for each channel/locale combination (only available since the 5.0 and when the \"with_quality_scores\" query parameter is set to \"true\")")
    completenesses: Optional[List[ProductsEmbeddedItemsInnerAllOf1CompletenessesInner]] = Field(None, description="Product completenesses for each channel/locale combination (only available since the 7.0 version, and when the \"with_completenesses\" query parameter is set to \"true\")")
    __properties = ["uuid", "identifier", "enabled", "family", "categories", "groups", "parent", "values", "associations", "quantified_associations", "created", "updated", "metadata", "quality_scores", "completenesses"]

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
    def from_json(cls, json_str: str) -> Product:
        """Create an instance of Product from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in values (dict)
        _field_dict = {}
        if self.values:
            for _key in self.values:
                if self.values[_key]:
                    _field_dict[_key] = self.values[_key].to_dict()
            _dict['values'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of associations
        if self.associations:
            _dict['associations'] = self.associations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of quantified_associations
        if self.quantified_associations:
            _dict['quantified_associations'] = self.quantified_associations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in completenesses (list)
        _items = []
        if self.completenesses:
            for _item in self.completenesses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['completenesses'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Product:
        """Create an instance of Product from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Product.parse_obj(obj)

        _obj = Product.parse_obj({
            "uuid": obj.get("uuid"),
            "identifier": obj.get("identifier"),
            "enabled": obj.get("enabled") if obj.get("enabled") is not None else True,
            "family": obj.get("family") if obj.get("family") is not None else 'null only in the case of a non variant product',
            "categories": obj.get("categories"),
            "groups": obj.get("groups"),
            "parent": obj.get("parent") if obj.get("parent") is not None else 'null',
            "values": dict((_k, Dict[str, List[ProductsEmbeddedItemsInnerAllOf1ValuesValueInner]].from_dict(_v)) for _k, _v in obj.get("values").items()),
            "associations": PostProductsRequestAssociations.from_dict(obj.get("associations")) if obj.get("associations") is not None else None,
            "quantified_associations": ProductsEmbeddedItemsInnerAllOf1QuantifiedAssociations.from_dict(obj.get("quantified_associations")) if obj.get("quantified_associations") is not None else None,
            "created": obj.get("created"),
            "updated": obj.get("updated"),
            "metadata": ProductsEmbeddedItemsInnerAllOf1Metadata.from_dict(obj.get("metadata")) if obj.get("metadata") is not None else None,
            "quality_scores": obj.get("quality_scores"),
            "completenesses": [ProductsEmbeddedItemsInnerAllOf1CompletenessesInner.from_dict(_item) for _item in obj.get("completenesses")] if obj.get("completenesses") is not None else None
        })
        return _obj

