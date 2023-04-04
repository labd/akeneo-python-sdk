# AssetFamiliesEmbeddedItemsInnerAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Asset family code | 
**labels** | [**AssetFamiliesEmbeddedItemsInnerAllOfLabels**](AssetFamiliesEmbeddedItemsInnerAllOfLabels.md) |  | [optional] 
**attribute_as_main_media** | **str** | Attribute code that is used as the main media of the asset family. | [optional] [default to 'First media file or media link attribute that was created']
**naming_convention** | [**AssetFamiliesEmbeddedItemsInnerAllOfNamingConvention**](AssetFamiliesEmbeddedItemsInnerAllOfNamingConvention.md) |  | [optional] 
**product_link_rules** | [**List[AssetFamiliesEmbeddedItemsInnerAllOfProductLinkRulesInner]**](AssetFamiliesEmbeddedItemsInnerAllOfProductLinkRulesInner.md) | The rules that will be run after the asset creation, in order to automatically link the assets of this family to a set of products. To understand the format of this property, see &lt;a href&#x3D;&#39;/concepts/asset-manager.html#focus-on-the-product-link-rule&#39;&gt;here&lt;/a&gt;. | [optional] 
**transformations** | [**List[AssetFamiliesEmbeddedItemsInnerAllOfTransformationsInner]**](AssetFamiliesEmbeddedItemsInnerAllOfTransformationsInner.md) | The transformations to perform on source files in order to generate new files into your asset attributes (only available since v4.0). To understand the format of this property, see &lt;a href&#x3D;&#39;/concepts/asset-manager.html#focus-on-the-transformations&#39;&gt;here&lt;/a&gt;. | [optional] 

## Example

```python
from akeneo.models.asset_families_embedded_items_inner_all_of import AssetFamiliesEmbeddedItemsInnerAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of AssetFamiliesEmbeddedItemsInnerAllOf from a JSON string
asset_families_embedded_items_inner_all_of_instance = AssetFamiliesEmbeddedItemsInnerAllOf.from_json(json)
# print the JSON string representation of the object
print AssetFamiliesEmbeddedItemsInnerAllOf.to_json()

# convert the object into a dict
asset_families_embedded_items_inner_all_of_dict = asset_families_embedded_items_inner_all_of_instance.to_dict()
# create an instance of AssetFamiliesEmbeddedItemsInnerAllOf from a dict
asset_families_embedded_items_inner_all_of_form_dict = asset_families_embedded_items_inner_all_of.from_dict(asset_families_embedded_items_inner_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


