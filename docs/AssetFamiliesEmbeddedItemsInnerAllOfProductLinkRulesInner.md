# AssetFamiliesEmbeddedItemsInnerAllOfProductLinkRulesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_selections** | [**List[AssetFamiliesEmbeddedItemsInnerAllOfProductLinkRulesInnerProductSelectionsInner]**](AssetFamiliesEmbeddedItemsInnerAllOfProductLinkRulesInnerProductSelectionsInner.md) | The product selection to which the assets of the asset family to be automatically linked. More details &lt;a href&#x3D;&#39;/concepts/asset-manager.html#product-selection&#39;&gt;here&lt;/a&gt;. | [optional] 
**assign_assets_to** | [**List[AssetFamiliesEmbeddedItemsInnerAllOfProductLinkRulesInnerAssignAssetsToInner]**](AssetFamiliesEmbeddedItemsInnerAllOfProductLinkRulesInnerAssignAssetsToInner.md) | The product value in which your assets will be assigned. More details &lt;a href&#x3D;&#39;/concepts/asset-manager.html#product-value-assignment&#39;&gt;here&lt;/a&gt;. | [optional] 

## Example

```python
from openapi_client.models.asset_families_embedded_items_inner_all_of_product_link_rules_inner import AssetFamiliesEmbeddedItemsInnerAllOfProductLinkRulesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AssetFamiliesEmbeddedItemsInnerAllOfProductLinkRulesInner from a JSON string
asset_families_embedded_items_inner_all_of_product_link_rules_inner_instance = AssetFamiliesEmbeddedItemsInnerAllOfProductLinkRulesInner.from_json(json)
# print the JSON string representation of the object
print AssetFamiliesEmbeddedItemsInnerAllOfProductLinkRulesInner.to_json()

# convert the object into a dict
asset_families_embedded_items_inner_all_of_product_link_rules_inner_dict = asset_families_embedded_items_inner_all_of_product_link_rules_inner_instance.to_dict()
# create an instance of AssetFamiliesEmbeddedItemsInnerAllOfProductLinkRulesInner from a dict
asset_families_embedded_items_inner_all_of_product_link_rules_inner_form_dict = asset_families_embedded_items_inner_all_of_product_link_rules_inner.from_dict(asset_families_embedded_items_inner_all_of_product_link_rules_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


