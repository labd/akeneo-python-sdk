# AttributeGroups


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**AttributeGroupsEmbedded**](AttributeGroupsEmbedded.md) |  | [optional] 
**links** | [**ProductsLinks**](ProductsLinks.md) |  | [optional] 
**current_page** | **int** | Current page number | [optional] 

## Example

```python
from akeneo.models.attribute_groups import AttributeGroups

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeGroups from a JSON string
attribute_groups_instance = AttributeGroups.from_json(json)
# print the JSON string representation of the object
print AttributeGroups.to_json()

# convert the object into a dict
attribute_groups_dict = attribute_groups_instance.to_dict()
# create an instance of AttributeGroups from a dict
attribute_groups_form_dict = attribute_groups.from_dict(attribute_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


