# ItemList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ProductsEmbeddedItemsInnerAllOfLinks**](ProductsEmbeddedItemsInnerAllOfLinks.md) |  | [optional] 

## Example

```python
from akeneo.models.item_list import ItemList

# TODO update the JSON string below
json = "{}"
# create an instance of ItemList from a JSON string
item_list_instance = ItemList.from_json(json)
# print the JSON string representation of the object
print ItemList.to_json()

# convert the object into a dict
item_list_dict = item_list_instance.to_dict()
# create an instance of ItemList from a dict
item_list_form_dict = item_list.from_dict(item_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


