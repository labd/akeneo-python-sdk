# GetAssetFamilyCode200ResponseProductLinkRulesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_selections** | [**List[GetAssetFamilyCode200ResponseProductLinkRulesInnerProductSelectionsInner]**](GetAssetFamilyCode200ResponseProductLinkRulesInnerProductSelectionsInner.md) | The product selection to which the assets of the asset family to be automatically linked. More details &lt;a href&#x3D;&#39;/concepts/asset-manager.html#product-selection&#39;&gt;here&lt;/a&gt;. | [optional] 
**assign_assets_to** | [**List[GetAssetFamilyCode200ResponseProductLinkRulesInnerAssignAssetsToInner]**](GetAssetFamilyCode200ResponseProductLinkRulesInnerAssignAssetsToInner.md) | The product value in which your assets will be assigned. More details &lt;a href&#x3D;&#39;/concepts/asset-manager.html#product-value-assignment&#39;&gt;here&lt;/a&gt;. | [optional] 

## Example

```python
from akeneo.models.get_asset_family_code200_response_product_link_rules_inner import GetAssetFamilyCode200ResponseProductLinkRulesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetFamilyCode200ResponseProductLinkRulesInner from a JSON string
get_asset_family_code200_response_product_link_rules_inner_instance = GetAssetFamilyCode200ResponseProductLinkRulesInner.from_json(json)
# print the JSON string representation of the object
print GetAssetFamilyCode200ResponseProductLinkRulesInner.to_json()

# convert the object into a dict
get_asset_family_code200_response_product_link_rules_inner_dict = get_asset_family_code200_response_product_link_rules_inner_instance.to_dict()
# create an instance of GetAssetFamilyCode200ResponseProductLinkRulesInner from a dict
get_asset_family_code200_response_product_link_rules_inner_form_dict = get_asset_family_code200_response_product_link_rules_inner.from_dict(get_asset_family_code200_response_product_link_rules_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


