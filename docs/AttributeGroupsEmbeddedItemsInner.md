# AttributeGroupsEmbeddedItemsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ProductsEmbeddedItemsInnerAllOfLinks**](ProductsEmbeddedItemsInnerAllOfLinks.md) |  | [optional] 
**code** | **str** | Attribute group code | 
**sort_order** | **int** | Attribute group order among other attribute groups | [optional] 
**attributes** | **List[str]** | Attribute codes that compose the attribute group | [optional] 
**labels** | [**AttributeGroupsEmbeddedItemsInnerAllOfLabels**](AttributeGroupsEmbeddedItemsInnerAllOfLabels.md) |  | [optional] 

## Example

```python
from akeneo.models.attribute_groups_embedded_items_inner import AttributeGroupsEmbeddedItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeGroupsEmbeddedItemsInner from a JSON string
attribute_groups_embedded_items_inner_instance = AttributeGroupsEmbeddedItemsInner.from_json(json)
# print the JSON string representation of the object
print AttributeGroupsEmbeddedItemsInner.to_json()

# convert the object into a dict
attribute_groups_embedded_items_inner_dict = attribute_groups_embedded_items_inner_instance.to_dict()
# create an instance of AttributeGroupsEmbeddedItemsInner from a dict
attribute_groups_embedded_items_inner_form_dict = attribute_groups_embedded_items_inner.from_dict(attribute_groups_embedded_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


