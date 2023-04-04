# AssetFamiliesEmbeddedItemsInnerAllOfTransformationsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The name of the transformation | 
**filename_suffix** | **str** | The suffix that will be appended to the source filename to generate the target filename. More details &lt;a href&#x3D;&#39;/concepts/asset-manager.html#target-filename&#39;&gt;here&lt;/a&gt;. | [optional] 
**filename_prefix** | **str** | The prefix that will be prepended to the source filename to generate the target filename. More details &lt;a href&#x3D;&#39;/concepts/asset-manager.html#target-filename&#39;&gt;here&lt;/a&gt;. | [optional] 
**source** | [**AssetFamiliesEmbeddedItemsInnerAllOfTransformationsInnerSource**](AssetFamiliesEmbeddedItemsInnerAllOfTransformationsInnerSource.md) |  | 
**target** | [**AssetFamiliesEmbeddedItemsInnerAllOfTransformationsInnerTarget**](AssetFamiliesEmbeddedItemsInnerAllOfTransformationsInnerTarget.md) |  | 
**operations** | [**AssetFamiliesEmbeddedItemsInnerAllOfTransformationsInnerOperations**](AssetFamiliesEmbeddedItemsInnerAllOfTransformationsInnerOperations.md) |  | 

## Example

```python
from openapi_client.models.asset_families_embedded_items_inner_all_of_transformations_inner import AssetFamiliesEmbeddedItemsInnerAllOfTransformationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AssetFamiliesEmbeddedItemsInnerAllOfTransformationsInner from a JSON string
asset_families_embedded_items_inner_all_of_transformations_inner_instance = AssetFamiliesEmbeddedItemsInnerAllOfTransformationsInner.from_json(json)
# print the JSON string representation of the object
print AssetFamiliesEmbeddedItemsInnerAllOfTransformationsInner.to_json()

# convert the object into a dict
asset_families_embedded_items_inner_all_of_transformations_inner_dict = asset_families_embedded_items_inner_all_of_transformations_inner_instance.to_dict()
# create an instance of AssetFamiliesEmbeddedItemsInnerAllOfTransformationsInner from a dict
asset_families_embedded_items_inner_all_of_transformations_inner_form_dict = asset_families_embedded_items_inner_all_of_transformations_inner.from_dict(asset_families_embedded_items_inner_all_of_transformations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


