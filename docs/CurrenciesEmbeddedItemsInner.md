# CurrenciesEmbeddedItemsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ProductsEmbeddedItemsInnerAllOfLinks**](ProductsEmbeddedItemsInnerAllOfLinks.md) |  | [optional] 
**code** | **str** | Currency code | 
**enabled** | **bool** | Whether the currency is enabled | [optional] 

## Example

```python
from openapi_client.models.currencies_embedded_items_inner import CurrenciesEmbeddedItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CurrenciesEmbeddedItemsInner from a JSON string
currencies_embedded_items_inner_instance = CurrenciesEmbeddedItemsInner.from_json(json)
# print the JSON string representation of the object
print CurrenciesEmbeddedItemsInner.to_json()

# convert the object into a dict
currencies_embedded_items_inner_dict = currencies_embedded_items_inner_instance.to_dict()
# create an instance of CurrenciesEmbeddedItemsInner from a dict
currencies_embedded_items_inner_form_dict = currencies_embedded_items_inner.from_dict(currencies_embedded_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


