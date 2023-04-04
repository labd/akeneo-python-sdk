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
from openapi_client.models.get_asset_family_code200_response_product_link_rules_inner_assign_assets_to_inner import GetAssetFamilyCode200ResponseProductLinkRulesInnerAssignAssetsToInner
from openapi_client.models.get_asset_family_code200_response_product_link_rules_inner_product_selections_inner import GetAssetFamilyCode200ResponseProductLinkRulesInnerProductSelectionsInner

class GetAssetFamilyCode200ResponseProductLinkRulesInner(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    product_selections: Optional[List[GetAssetFamilyCode200ResponseProductLinkRulesInnerProductSelectionsInner]] = Field(None, description="The product selection to which the assets of the asset family to be automatically linked. More details <a href='/concepts/asset-manager.html#product-selection'>here</a>.")
    assign_assets_to: Optional[List[GetAssetFamilyCode200ResponseProductLinkRulesInnerAssignAssetsToInner]] = Field(None, description="The product value in which your assets will be assigned. More details <a href='/concepts/asset-manager.html#product-value-assignment'>here</a>.")
    __properties = ["product_selections", "assign_assets_to"]

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
    def from_json(cls, json_str: str) -> GetAssetFamilyCode200ResponseProductLinkRulesInner:
        """Create an instance of GetAssetFamilyCode200ResponseProductLinkRulesInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in product_selections (list)
        _items = []
        if self.product_selections:
            for _item in self.product_selections:
                if _item:
                    _items.append(_item.to_dict())
            _dict['product_selections'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in assign_assets_to (list)
        _items = []
        if self.assign_assets_to:
            for _item in self.assign_assets_to:
                if _item:
                    _items.append(_item.to_dict())
            _dict['assign_assets_to'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetAssetFamilyCode200ResponseProductLinkRulesInner:
        """Create an instance of GetAssetFamilyCode200ResponseProductLinkRulesInner from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return GetAssetFamilyCode200ResponseProductLinkRulesInner.parse_obj(obj)

        _obj = GetAssetFamilyCode200ResponseProductLinkRulesInner.parse_obj({
            "product_selections": [GetAssetFamilyCode200ResponseProductLinkRulesInnerProductSelectionsInner.from_dict(_item) for _item in obj.get("product_selections")] if obj.get("product_selections") is not None else None,
            "assign_assets_to": [GetAssetFamilyCode200ResponseProductLinkRulesInnerAssignAssetsToInner.from_dict(_item) for _item in obj.get("assign_assets_to")] if obj.get("assign_assets_to") is not None else None
        })
        return _obj

