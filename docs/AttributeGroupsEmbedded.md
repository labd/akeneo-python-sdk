# AttributeGroupsEmbedded


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AttributeGroupsEmbeddedItemsInner]**](AttributeGroupsEmbeddedItemsInner.md) |  | [optional] 

## Example

```python
from akeneo.models.attribute_groups_embedded import AttributeGroupsEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeGroupsEmbedded from a JSON string
attribute_groups_embedded_instance = AttributeGroupsEmbedded.from_json(json)
# print the JSON string representation of the object
print AttributeGroupsEmbedded.to_json()

# convert the object into a dict
attribute_groups_embedded_dict = attribute_groups_embedded_instance.to_dict()
# create an instance of AttributeGroupsEmbedded from a dict
attribute_groups_embedded_form_dict = attribute_groups_embedded.from_dict(attribute_groups_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


