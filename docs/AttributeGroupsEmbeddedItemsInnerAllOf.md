# AttributeGroupsEmbeddedItemsInnerAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Attribute group code | 
**sort_order** | **int** | Attribute group order among other attribute groups | [optional] 
**attributes** | **List[str]** | Attribute codes that compose the attribute group | [optional] 
**labels** | [**AttributeGroupsEmbeddedItemsInnerAllOfLabels**](AttributeGroupsEmbeddedItemsInnerAllOfLabels.md) |  | [optional] 

## Example

```python
from openapi_client.models.attribute_groups_embedded_items_inner_all_of import AttributeGroupsEmbeddedItemsInnerAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeGroupsEmbeddedItemsInnerAllOf from a JSON string
attribute_groups_embedded_items_inner_all_of_instance = AttributeGroupsEmbeddedItemsInnerAllOf.from_json(json)
# print the JSON string representation of the object
print AttributeGroupsEmbeddedItemsInnerAllOf.to_json()

# convert the object into a dict
attribute_groups_embedded_items_inner_all_of_dict = attribute_groups_embedded_items_inner_all_of_instance.to_dict()
# create an instance of AttributeGroupsEmbeddedItemsInnerAllOf from a dict
attribute_groups_embedded_items_inner_all_of_form_dict = attribute_groups_embedded_items_inner_all_of.from_dict(attribute_groups_embedded_items_inner_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


