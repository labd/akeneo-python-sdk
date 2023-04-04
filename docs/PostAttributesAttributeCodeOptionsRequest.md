# PostAttributesAttributeCodeOptionsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code of option | 
**attribute** | **str** | Code of attribute related to the attribute option | [optional] 
**sort_order** | **int** | Order of attribute option | [optional] 
**labels** | [**PostAttributesAttributeCodeOptionsRequestLabels**](PostAttributesAttributeCodeOptionsRequestLabels.md) |  | [optional] 

## Example

```python
from akeneo.models.post_attributes_attribute_code_options_request import PostAttributesAttributeCodeOptionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostAttributesAttributeCodeOptionsRequest from a JSON string
post_attributes_attribute_code_options_request_instance = PostAttributesAttributeCodeOptionsRequest.from_json(json)
# print the JSON string representation of the object
print PostAttributesAttributeCodeOptionsRequest.to_json()

# convert the object into a dict
post_attributes_attribute_code_options_request_dict = post_attributes_attribute_code_options_request_instance.to_dict()
# create an instance of PostAttributesAttributeCodeOptionsRequest from a dict
post_attributes_attribute_code_options_request_form_dict = post_attributes_attribute_code_options_request.from_dict(post_attributes_attribute_code_options_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


