# AssetEmbeddedItemsInnerAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code of the asset | 
**values** | **Dict[str, List[AssetEmbeddedItemsInnerAllOfValuesValueInner]]** | Asset attributes values, see the &lt;a href&#x3D;&#39;/concepts/asset-manager.html#focus-on-the-asset-values&#39;&gt;Focus on the asset values&lt;/a&gt; section for more details. | [optional] 
**created** | **str** | Date of creation | [optional] 
**updated** | **str** | Date of the last update | [optional] 

## Example

```python
from openapi_client.models.asset_embedded_items_inner_all_of import AssetEmbeddedItemsInnerAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of AssetEmbeddedItemsInnerAllOf from a JSON string
asset_embedded_items_inner_all_of_instance = AssetEmbeddedItemsInnerAllOf.from_json(json)
# print the JSON string representation of the object
print AssetEmbeddedItemsInnerAllOf.to_json()

# convert the object into a dict
asset_embedded_items_inner_all_of_dict = asset_embedded_items_inner_all_of_instance.to_dict()
# create an instance of AssetEmbeddedItemsInnerAllOf from a dict
asset_embedded_items_inner_all_of_form_dict = asset_embedded_items_inner_all_of.from_dict(asset_embedded_items_inner_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


