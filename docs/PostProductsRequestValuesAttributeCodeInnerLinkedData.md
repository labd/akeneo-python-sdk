# PostProductsRequestValuesAttributeCodeInnerLinkedData

Object containing labels of attribute options (only available since the 5.0 and when query parameter \"with_attribute_options\" is set to \"true\"). See <a href='/concepts/products.html#the-linked_data-format'>the `linked_data` format</a> section for more details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**labels** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.post_products_request_values_attribute_code_inner_linked_data import PostProductsRequestValuesAttributeCodeInnerLinkedData

# TODO update the JSON string below
json = "{}"
# create an instance of PostProductsRequestValuesAttributeCodeInnerLinkedData from a JSON string
post_products_request_values_attribute_code_inner_linked_data_instance = PostProductsRequestValuesAttributeCodeInnerLinkedData.from_json(json)
# print the JSON string representation of the object
print PostProductsRequestValuesAttributeCodeInnerLinkedData.to_json()

# convert the object into a dict
post_products_request_values_attribute_code_inner_linked_data_dict = post_products_request_values_attribute_code_inner_linked_data_instance.to_dict()
# create an instance of PostProductsRequestValuesAttributeCodeInnerLinkedData from a dict
post_products_request_values_attribute_code_inner_linked_data_form_dict = post_products_request_values_attribute_code_inner_linked_data.from_dict(post_products_request_values_attribute_code_inner_linked_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


