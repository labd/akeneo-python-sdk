# ReferenceEntityItemList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ReferenceEntitiesEmbeddedItemsInnerAllOfLinks**](ReferenceEntitiesEmbeddedItemsInnerAllOfLinks.md) |  | [optional] 

## Example

```python
from akeneo.models.reference_entity_item_list import ReferenceEntityItemList

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceEntityItemList from a JSON string
reference_entity_item_list_instance = ReferenceEntityItemList.from_json(json)
# print the JSON string representation of the object
print ReferenceEntityItemList.to_json()

# convert the object into a dict
reference_entity_item_list_dict = reference_entity_item_list_instance.to_dict()
# create an instance of ReferenceEntityItemList from a dict
reference_entity_item_list_form_dict = reference_entity_item_list.from_dict(reference_entity_item_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


