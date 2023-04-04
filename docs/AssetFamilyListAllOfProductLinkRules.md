# AssetFamilyListAllOfProductLinkRules


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_selections** | [**List[AssetFamilyListAllOfProductSelections]**](AssetFamilyListAllOfProductSelections.md) | The product selection to which the assets of the asset family to be automatically linked. More details &lt;a href&#x3D;&#39;/concepts/asset-manager.html#product-selection&#39;&gt;here&lt;/a&gt;. | [optional] 
**assign_assets_to** | [**List[AssetFamilyListAllOfAssignAssetsTo]**](AssetFamilyListAllOfAssignAssetsTo.md) | The product value in which your assets will be assigned. More details &lt;a href&#x3D;&#39;/concepts/asset-manager.html#product-value-assignment&#39;&gt;here&lt;/a&gt;. | [optional] 

## Example

```python
from openapi_client.models.asset_family_list_all_of_product_link_rules import AssetFamilyListAllOfProductLinkRules

# TODO update the JSON string below
json = "{}"
# create an instance of AssetFamilyListAllOfProductLinkRules from a JSON string
asset_family_list_all_of_product_link_rules_instance = AssetFamilyListAllOfProductLinkRules.from_json(json)
# print the JSON string representation of the object
print AssetFamilyListAllOfProductLinkRules.to_json()

# convert the object into a dict
asset_family_list_all_of_product_link_rules_dict = asset_family_list_all_of_product_link_rules_instance.to_dict()
# create an instance of AssetFamilyListAllOfProductLinkRules from a dict
asset_family_list_all_of_product_link_rules_form_dict = asset_family_list_all_of_product_link_rules.from_dict(asset_family_list_all_of_product_link_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


