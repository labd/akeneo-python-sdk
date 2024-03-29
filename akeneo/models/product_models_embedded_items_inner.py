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
from pydantic import BaseModel, Field, StrictStr
from akeneo.models.product_models_embedded_items_inner_all_of_associations import ProductModelsEmbeddedItemsInnerAllOfAssociations
from akeneo.models.product_models_embedded_items_inner_all_of_metadata import ProductModelsEmbeddedItemsInnerAllOfMetadata
from akeneo.models.product_models_embedded_items_inner_all_of_quantified_associations import ProductModelsEmbeddedItemsInnerAllOfQuantifiedAssociations
from akeneo.models.product_models_embedded_items_inner_all_of_values_value_inner import ProductModelsEmbeddedItemsInnerAllOfValuesValueInner
from akeneo.models.products_embedded_items_inner_all_of_links import ProductsEmbeddedItemsInnerAllOfLinks

class ProductModelsEmbeddedItemsInner(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    links: Optional[ProductsEmbeddedItemsInnerAllOfLinks] = Field(None, alias="_links")
    code: StrictStr = Field(..., description="Product model code")
    family: Optional[StrictStr] = Field(None, description="<a href='api-reference.html#Family'>Family</a> code  from which the product inherits its attributes and attributes requirements (since the 3.2)")
    family_variant: StrictStr = Field(..., description="Family variant code from which the product model inherits its attributes and variant attributes")
    parent: Optional[StrictStr] = Field('null', description="Code of the parent <a href='api-reference.html#Productmodel'>product model</a>. This parent can be modified since the 2.3.")
    categories: Optional[List[StrictStr]] = Field(None, description="Codes of the <a href='api-reference.html#Category'>categories</a> in which the product model is categorized")
    values: Optional[Dict[str, List[ProductModelsEmbeddedItemsInnerAllOfValuesValueInner]]] = Field(None, description="Product model attributes values, see <a href='/concepts/products.html#focus-on-the-product-values'>Product values</a> section for more details")
    associations: Optional[ProductModelsEmbeddedItemsInnerAllOfAssociations] = None
    quantified_associations: Optional[ProductModelsEmbeddedItemsInnerAllOfQuantifiedAssociations] = None
    created: Optional[StrictStr] = Field(None, description="Date of creation")
    updated: Optional[StrictStr] = Field(None, description="Date of the last update")
    metadata: Optional[ProductModelsEmbeddedItemsInnerAllOfMetadata] = None
    quality_scores: Optional[Dict[str, Any]] = Field(None, description="Product model quality scores for each channel/locale combination (<strong>only available since the 7.0 version</strong> and when the \"with_quality_scores\" query parameter is set to \"true\")")
    __properties = ["_links", "code", "family", "family_variant", "parent", "categories", "values", "associations", "quantified_associations", "created", "updated", "metadata", "quality_scores"]

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
    def from_json(cls, json_str: str) -> ProductModelsEmbeddedItemsInner:
        """Create an instance of ProductModelsEmbeddedItemsInner from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProductModelsEmbeddedItemsInner:
        """Create an instance of ProductModelsEmbeddedItemsInner from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ProductModelsEmbeddedItemsInner.parse_obj(obj)

        _obj = ProductModelsEmbeddedItemsInner.parse_obj({
            "links": ProductsEmbeddedItemsInnerAllOfLinks.from_dict(obj.get("_links")) if obj.get("_links") is not None else None,
            "code": obj.get("code"),
            "family": obj.get("family"),
            "family_variant": obj.get("family_variant"),
            "parent": obj.get("parent") if obj.get("parent") is not None else 'null',
            "categories": obj.get("categories"),
            "values": dict((_k, [ProductModelsEmbeddedItemsInnerAllOfValuesValueInner.from_dict(_item) for _item in _v]) for _k, _v in obj.get("values").items()),
            "associations": ProductModelsEmbeddedItemsInnerAllOfAssociations.from_dict(obj.get("associations")) if obj.get("associations") is not None else None,
            "quantified_associations": ProductModelsEmbeddedItemsInnerAllOfQuantifiedAssociations.from_dict(obj.get("quantified_associations")) if obj.get("quantified_associations") is not None else None,
            "created": obj.get("created"),
            "updated": obj.get("updated"),
            "metadata": ProductModelsEmbeddedItemsInnerAllOfMetadata.from_dict(obj.get("metadata")) if obj.get("metadata") is not None else None,
            "quality_scores": obj.get("quality_scores")
        })
        return _obj

