# Currencies


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**CurrenciesEmbedded**](CurrenciesEmbedded.md) |  | [optional] 
**links** | [**ProductsLinks**](ProductsLinks.md) |  | [optional] 
**current_page** | **int** | Current page number | [optional] 

## Example

```python
from akeneo.models.currencies import Currencies

# TODO update the JSON string below
json = "{}"
# create an instance of Currencies from a JSON string
currencies_instance = Currencies.from_json(json)
# print the JSON string representation of the object
print Currencies.to_json()

# convert the object into a dict
currencies_dict = currencies_instance.to_dict()
# create an instance of Currencies from a dict
currencies_form_dict = currencies.from_dict(currencies_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


