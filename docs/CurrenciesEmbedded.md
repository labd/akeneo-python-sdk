# CurrenciesEmbedded


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CurrenciesEmbeddedItemsInner]**](CurrenciesEmbeddedItemsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.currencies_embedded import CurrenciesEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of CurrenciesEmbedded from a JSON string
currencies_embedded_instance = CurrenciesEmbedded.from_json(json)
# print the JSON string representation of the object
print CurrenciesEmbedded.to_json()

# convert the object into a dict
currencies_embedded_dict = currencies_embedded_instance.to_dict()
# create an instance of CurrenciesEmbedded from a dict
currencies_embedded_form_dict = currencies_embedded.from_dict(currencies_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


