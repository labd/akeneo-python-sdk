# PostProductsRequestValues

Product attributes values, see <a href='/concepts/products.html#focus-on-the-product-values'>Product values</a> section for more details

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_code** | [**List[PostProductsRequestValuesAttributeCodeInner]**](PostProductsRequestValuesAttributeCodeInner.md) |  | [optional] 

## Example

```python
from akeneo.models.post_products_request_values import PostProductsRequestValues

# TODO update the JSON string below
json = "{}"
# create an instance of PostProductsRequestValues from a JSON string
post_products_request_values_instance = PostProductsRequestValues.from_json(json)
# print the JSON string representation of the object
print PostProductsRequestValues.to_json()

# convert the object into a dict
post_products_request_values_dict = post_products_request_values_instance.to_dict()
# create an instance of PostProductsRequestValues from a dict
post_products_request_values_form_dict = post_products_request_values.from_dict(post_products_request_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


