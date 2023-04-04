# AttributeGroupListAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Attribute group code | 
**sort_order** | **int** | Attribute group order among other attribute groups | [optional] 
**attributes** | **List[str]** | Attribute codes that compose the attribute group | [optional] 
**labels** | [**AttributeGroupListAllOfLabels**](AttributeGroupListAllOfLabels.md) |  | [optional] 

## Example

```python
from openapi_client.models.attribute_group_list_all_of import AttributeGroupListAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeGroupListAllOf from a JSON string
attribute_group_list_all_of_instance = AttributeGroupListAllOf.from_json(json)
# print the JSON string representation of the object
print AttributeGroupListAllOf.to_json()

# convert the object into a dict
attribute_group_list_all_of_dict = attribute_group_list_all_of_instance.to_dict()
# create an instance of AttributeGroupListAllOf from a dict
attribute_group_list_all_of_form_dict = attribute_group_list_all_of.from_dict(attribute_group_list_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


