# PostProductModelsRequestValuesAttributeCodeInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | &lt;a href&#x3D;&#39;api-reference.html#Channel&#39;&gt;Channel&lt;/a&gt; code of the product value | [optional] 
**locale** | **str** | &lt;a href&#x3D;&#39;api-reference.html#Locale&#39;&gt;Locale&lt;/a&gt; code of the product value | [optional] 
**data** | **object** | &lt;a href&#x3D;&#39;api-reference.html#Productuuid&#39;&gt;Product&lt;/a&gt; value | [optional] 

## Example

```python
from openapi_client.models.post_product_models_request_values_attribute_code_inner import PostProductModelsRequestValuesAttributeCodeInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostProductModelsRequestValuesAttributeCodeInner from a JSON string
post_product_models_request_values_attribute_code_inner_instance = PostProductModelsRequestValuesAttributeCodeInner.from_json(json)
# print the JSON string representation of the object
print PostProductModelsRequestValuesAttributeCodeInner.to_json()

# convert the object into a dict
post_product_models_request_values_attribute_code_inner_dict = post_product_models_request_values_attribute_code_inner_instance.to_dict()
# create an instance of PostProductModelsRequestValuesAttributeCodeInner from a dict
post_product_models_request_values_attribute_code_inner_form_dict = post_product_models_request_values_attribute_code_inner.from_dict(post_product_models_request_values_attribute_code_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


