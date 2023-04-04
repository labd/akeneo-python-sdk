# AttributeListAllOfValidations

User defined validation constraints on the cell content

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **float** | minimum value of a numeric cell | [optional] 
**max** | **float** | maximum value of a numeric cell | [optional] 
**decimals_allowed** | **bool** | whether the value of a numeric cell can hold a decimal part | [optional] 
**max_length** | **float** | maximum length of a text cell | [optional] 

## Example

```python
from openapi_client.models.attribute_list_all_of_validations import AttributeListAllOfValidations

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeListAllOfValidations from a JSON string
attribute_list_all_of_validations_instance = AttributeListAllOfValidations.from_json(json)
# print the JSON string representation of the object
print AttributeListAllOfValidations.to_json()

# convert the object into a dict
attribute_list_all_of_validations_dict = attribute_list_all_of_validations_instance.to_dict()
# create an instance of AttributeListAllOfValidations from a dict
attribute_list_all_of_validations_form_dict = attribute_list_all_of_validations.from_dict(attribute_list_all_of_validations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


