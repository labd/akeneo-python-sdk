# GetPublishedProductsCode200ResponseValues

Published product attributes values, see <a href='/concepts/products.html#focus-on-the-product-values'>Product values</a> section for more details

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_code** | [**List[PostProductModelsRequestValuesAttributeCodeInner]**](PostProductModelsRequestValuesAttributeCodeInner.md) |  | [optional] 

## Example

```python
from akeneo.models.get_published_products_code200_response_values import GetPublishedProductsCode200ResponseValues

# TODO update the JSON string below
json = "{}"
# create an instance of GetPublishedProductsCode200ResponseValues from a JSON string
get_published_products_code200_response_values_instance = GetPublishedProductsCode200ResponseValues.from_json(json)
# print the JSON string representation of the object
print GetPublishedProductsCode200ResponseValues.to_json()

# convert the object into a dict
get_published_products_code200_response_values_dict = get_published_products_code200_response_values_instance.to_dict()
# create an instance of GetPublishedProductsCode200ResponseValues from a dict
get_published_products_code200_response_values_form_dict = get_published_products_code200_response_values.from_dict(get_published_products_code200_response_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


