# PostAttributesRequestTableConfigurationInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Column code | 
**data_type** | **str** | Column data type | 
**validations** | [**PostAttributesRequestTableConfigurationInnerValidations**](PostAttributesRequestTableConfigurationInnerValidations.md) |  | [optional] 
**labels** | [**PostAttributesRequestTableConfigurationInnerLabels**](PostAttributesRequestTableConfigurationInnerLabels.md) |  | [optional] 
**is_required_for_completeness** | **bool** | Defines if the column should be entirely filled for the attribute to be considered complete | [optional] [default to False]

## Example

```python
from akeneo.models.post_attributes_request_table_configuration_inner import PostAttributesRequestTableConfigurationInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostAttributesRequestTableConfigurationInner from a JSON string
post_attributes_request_table_configuration_inner_instance = PostAttributesRequestTableConfigurationInner.from_json(json)
# print the JSON string representation of the object
print PostAttributesRequestTableConfigurationInner.to_json()

# convert the object into a dict
post_attributes_request_table_configuration_inner_dict = post_attributes_request_table_configuration_inner_instance.to_dict()
# create an instance of PostAttributesRequestTableConfigurationInner from a dict
post_attributes_request_table_configuration_inner_form_dict = post_attributes_request_table_configuration_inner.from_dict(post_attributes_request_table_configuration_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


