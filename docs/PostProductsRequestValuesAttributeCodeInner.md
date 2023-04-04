# PostProductsRequestValuesAttributeCodeInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | &lt;a href&#x3D;&#39;api-reference.html#Channel&#39;&gt;Channel&lt;/a&gt; code of the product value | [optional] 
**locale** | **str** | &lt;a href&#x3D;&#39;api-reference.html#Locale&#39;&gt;Locale&lt;/a&gt; code of the product value | [optional] 
**data** | **object** | Product value. See &lt;a href&#x3D;&#39;/concepts/products.html#the-data-format&#39;&gt;the &#x60;data&#x60; format&lt;/a&gt; section for more details. | [optional] 
**linked_data** | [**PostProductsRequestValuesAttributeCodeInnerLinkedData**](PostProductsRequestValuesAttributeCodeInnerLinkedData.md) |  | [optional] 

## Example

```python
from openapi_client.models.post_products_request_values_attribute_code_inner import PostProductsRequestValuesAttributeCodeInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostProductsRequestValuesAttributeCodeInner from a JSON string
post_products_request_values_attribute_code_inner_instance = PostProductsRequestValuesAttributeCodeInner.from_json(json)
# print the JSON string representation of the object
print PostProductsRequestValuesAttributeCodeInner.to_json()

# convert the object into a dict
post_products_request_values_attribute_code_inner_dict = post_products_request_values_attribute_code_inner_instance.to_dict()
# create an instance of PostProductsRequestValuesAttributeCodeInner from a dict
post_products_request_values_attribute_code_inner_form_dict = post_products_request_values_attribute_code_inner.from_dict(post_products_request_values_attribute_code_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


