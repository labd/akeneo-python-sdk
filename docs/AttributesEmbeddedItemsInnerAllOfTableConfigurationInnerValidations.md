# AttributesEmbeddedItemsInnerAllOfTableConfigurationInnerValidations

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
from akeneo.models.attributes_embedded_items_inner_all_of_table_configuration_inner_validations import AttributesEmbeddedItemsInnerAllOfTableConfigurationInnerValidations

# TODO update the JSON string below
json = "{}"
# create an instance of AttributesEmbeddedItemsInnerAllOfTableConfigurationInnerValidations from a JSON string
attributes_embedded_items_inner_all_of_table_configuration_inner_validations_instance = AttributesEmbeddedItemsInnerAllOfTableConfigurationInnerValidations.from_json(json)
# print the JSON string representation of the object
print AttributesEmbeddedItemsInnerAllOfTableConfigurationInnerValidations.to_json()

# convert the object into a dict
attributes_embedded_items_inner_all_of_table_configuration_inner_validations_dict = attributes_embedded_items_inner_all_of_table_configuration_inner_validations_instance.to_dict()
# create an instance of AttributesEmbeddedItemsInnerAllOfTableConfigurationInnerValidations from a dict
attributes_embedded_items_inner_all_of_table_configuration_inner_validations_form_dict = attributes_embedded_items_inner_all_of_table_configuration_inner_validations.from_dict(attributes_embedded_items_inner_all_of_table_configuration_inner_validations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


