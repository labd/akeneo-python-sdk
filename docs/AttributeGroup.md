# AttributeGroup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Attribute group code | 
**sort_order** | **int** | Attribute group order among other attribute groups | [optional] 
**attributes** | **List[str]** | Attribute codes that compose the attribute group | [optional] 
**labels** | [**AttributeGroupsEmbeddedItemsInnerAllOfLabels**](AttributeGroupsEmbeddedItemsInnerAllOfLabels.md) |  | [optional] 

## Example

```python
from akeneo.models.attribute_group import AttributeGroup

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeGroup from a JSON string
attribute_group_instance = AttributeGroup.from_json(json)
# print the JSON string representation of the object
print AttributeGroup.to_json()

# convert the object into a dict
attribute_group_dict = attribute_group_instance.to_dict()
# create an instance of AttributeGroup from a dict
attribute_group_form_dict = attribute_group.from_dict(attribute_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


