# AttributesEmbeddedItemsInnerAllOfTableConfigurationInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Column code | 
**data_type** | **str** | Column data type | 
**validations** | [**AttributesEmbeddedItemsInnerAllOfTableConfigurationInnerValidations**](AttributesEmbeddedItemsInnerAllOfTableConfigurationInnerValidations.md) |  | [optional] 
**labels** | [**AttributesEmbeddedItemsInnerAllOfTableConfigurationInnerLabels**](AttributesEmbeddedItemsInnerAllOfTableConfigurationInnerLabels.md) |  | [optional] 
**is_required_for_completeness** | **bool** | Defines if the column should be entirely filled for the attribute to be considered complete | [optional] [default to False]

## Example

```python
from openapi_client.models.attributes_embedded_items_inner_all_of_table_configuration_inner import AttributesEmbeddedItemsInnerAllOfTableConfigurationInner

# TODO update the JSON string below
json = "{}"
# create an instance of AttributesEmbeddedItemsInnerAllOfTableConfigurationInner from a JSON string
attributes_embedded_items_inner_all_of_table_configuration_inner_instance = AttributesEmbeddedItemsInnerAllOfTableConfigurationInner.from_json(json)
# print the JSON string representation of the object
print AttributesEmbeddedItemsInnerAllOfTableConfigurationInner.to_json()

# convert the object into a dict
attributes_embedded_items_inner_all_of_table_configuration_inner_dict = attributes_embedded_items_inner_all_of_table_configuration_inner_instance.to_dict()
# create an instance of AttributesEmbeddedItemsInnerAllOfTableConfigurationInner from a dict
attributes_embedded_items_inner_all_of_table_configuration_inner_form_dict = attributes_embedded_items_inner_all_of_table_configuration_inner.from_dict(attributes_embedded_items_inner_all_of_table_configuration_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


