# AttributeOptionList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ProductListAllOfLinks**](ProductListAllOfLinks.md) |  | [optional] 
**code** | **str** | Code of option | 
**attribute** | **str** | Code of attribute related to the attribute option | [optional] 
**sort_order** | **int** | Order of attribute option | [optional] 
**labels** | [**AttributeOptionListAllOfLabels**](AttributeOptionListAllOfLabels.md) |  | [optional] 

## Example

```python
from akeneo.models.attribute_option_list import AttributeOptionList

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeOptionList from a JSON string
attribute_option_list_instance = AttributeOptionList.from_json(json)
# print the JSON string representation of the object
print AttributeOptionList.to_json()

# convert the object into a dict
attribute_option_list_dict = attribute_option_list_instance.to_dict()
# create an instance of AttributeOptionList from a dict
attribute_option_list_form_dict = attribute_option_list.from_dict(attribute_option_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


