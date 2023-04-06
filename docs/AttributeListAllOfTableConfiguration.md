# AttributeListAllOfTableConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Column code | 
**data_type** | **str** | Column data type | 
**validations** | [**AttributeListAllOfValidations**](AttributeListAllOfValidations.md) |  | [optional] 
**labels** | [**AttributeListAllOfLabels**](AttributeListAllOfLabels.md) |  | [optional] 
**is_required_for_completeness** | **bool** | Defines if the column should be entirely filled for the attribute to be considered complete | [optional] [default to False]

## Example

```python
from akeneo.models.attribute_list_all_of_table_configuration import AttributeListAllOfTableConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeListAllOfTableConfiguration from a JSON string
attribute_list_all_of_table_configuration_instance = AttributeListAllOfTableConfiguration.from_json(json)
# print the JSON string representation of the object
print AttributeListAllOfTableConfiguration.to_json()

# convert the object into a dict
attribute_list_all_of_table_configuration_dict = attribute_list_all_of_table_configuration_instance.to_dict()
# create an instance of AttributeListAllOfTableConfiguration from a dict
attribute_list_all_of_table_configuration_form_dict = attribute_list_all_of_table_configuration.from_dict(attribute_list_all_of_table_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


