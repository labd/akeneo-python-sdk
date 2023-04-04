# AttributeOptionListAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code of option | 
**attribute** | **str** | Code of attribute related to the attribute option | [optional] 
**sort_order** | **int** | Order of attribute option | [optional] 
**labels** | [**AttributeOptionListAllOfLabels**](AttributeOptionListAllOfLabels.md) |  | [optional] 

## Example

```python
from openapi_client.models.attribute_option_list_all_of import AttributeOptionListAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeOptionListAllOf from a JSON string
attribute_option_list_all_of_instance = AttributeOptionListAllOf.from_json(json)
# print the JSON string representation of the object
print AttributeOptionListAllOf.to_json()

# convert the object into a dict
attribute_option_list_all_of_dict = attribute_option_list_all_of_instance.to_dict()
# create an instance of AttributeOptionListAllOf from a dict
attribute_option_list_all_of_form_dict = attribute_option_list_all_of.from_dict(attribute_option_list_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


