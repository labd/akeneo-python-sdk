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
from openapi_client.models.product_models_embedded_items_inner_all_of_values_value_inner import ProductModelsEmbeddedItemsInnerAllOfValuesValueInner
from openapi_client.models.published_products_embedded_items_inner_all_of_associations import PublishedProductsEmbeddedItemsInnerAllOfAssociations

class PublishedProduct(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    identifier: StrictStr = Field(..., description="Published product identifier, i.e. the value of the only `pim_catalog_identifier` attribute")
    enabled: Optional[StrictBool] = Field(True, description="Whether the published product is enable")
    family: Optional[StrictStr] = Field('null', description="<a href='api-reference.html#Family'>Family</a> code from which the published product inherits its attributes and attributes requirements")
    categories: Optional[List[StrictStr]] = Field(None, description="Codes of the <a href='api-reference.html#Category'>categories</a> in which the published product is classified")
    groups: Optional[List[StrictStr]] = Field(None, description="Codes of the groups to which the published product belong")
    values: Optional[Dict[str, List[ProductModelsEmbeddedItemsInnerAllOfValuesValueInner]]] = Field(None, description="Published product attributes values, see <a href='/concepts/products.html#focus-on-the-product-values'>Product values</a> section for more details")
    associations: Optional[PublishedProductsEmbeddedItemsInnerAllOfAssociations] = None
    quantified_associations: Optional[Dict[str, Any]] = Field(None, description="Warning: associations with quantities are not compatible with the published products. The response will always be empty.")
    created: Optional[StrictStr] = Field(None, description="Date of creation")
    updated: Optional[StrictStr] = Field(None, description="Date of the last update")
    __properties = ["identifier", "enabled", "family", "categories", "groups", "values", "associations", "quantified_associations", "created", "updated"]

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
    def from_json(cls, json_str: str) -> PublishedProduct:
        """Create an instance of PublishedProduct from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PublishedProduct:
        """Create an instance of PublishedProduct from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return PublishedProduct.parse_obj(obj)

        _obj = PublishedProduct.parse_obj({
            "identifier": obj.get("identifier"),
            "enabled": obj.get("enabled") if obj.get("enabled") is not None else True,
            "family": obj.get("family") if obj.get("family") is not None else 'null',
            "categories": obj.get("categories"),
            "groups": obj.get("groups"),
            "values": dict((_k, Dict[str, List[ProductModelsEmbeddedItemsInnerAllOfValuesValueInner]].from_dict(_v)) for _k, _v in obj.get("values").items()),
            "associations": PublishedProductsEmbeddedItemsInnerAllOfAssociations.from_dict(obj.get("associations")) if obj.get("associations") is not None else None,
            "quantified_associations": obj.get("quantified_associations"),
            "created": obj.get("created"),
            "updated": obj.get("updated")
        })
        return _obj

