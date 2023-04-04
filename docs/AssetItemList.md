# AssetItemList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ProductsEmbeddedItemsInnerAllOfLinks**](ProductsEmbeddedItemsInnerAllOfLinks.md) |  | [optional] 

## Example

```python
from akeneo.models.asset_item_list import AssetItemList

# TODO update the JSON string below
json = "{}"
# create an instance of AssetItemList from a JSON string
asset_item_list_instance = AssetItemList.from_json(json)
# print the JSON string representation of the object
print AssetItemList.to_json()

# convert the object into a dict
asset_item_list_dict = asset_item_list_instance.to_dict()
# create an instance of AssetItemList from a dict
asset_item_list_form_dict = asset_item_list.from_dict(asset_item_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


