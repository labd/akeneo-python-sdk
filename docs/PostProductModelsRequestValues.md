# PostProductModelsRequestValues

Product model attributes values, see <a href='/concepts/products.html#focus-on-the-product-values'>Product values</a> section for more details

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_code** | [**List[PostProductModelsRequestValuesAttributeCodeInner]**](PostProductModelsRequestValuesAttributeCodeInner.md) |  | [optional] 

## Example

```python
from akeneo.models.post_product_models_request_values import PostProductModelsRequestValues

# TODO update the JSON string below
json = "{}"
# create an instance of PostProductModelsRequestValues from a JSON string
post_product_models_request_values_instance = PostProductModelsRequestValues.from_json(json)
# print the JSON string representation of the object
print PostProductModelsRequestValues.to_json()

# convert the object into a dict
post_product_models_request_values_dict = post_product_models_request_values_instance.to_dict()
# create an instance of PostProductModelsRequestValues from a dict
post_product_models_request_values_form_dict = post_product_models_request_values.from_dict(post_product_models_request_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


