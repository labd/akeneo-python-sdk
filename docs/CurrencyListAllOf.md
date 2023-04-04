# CurrencyListAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Currency code | 
**enabled** | **bool** | Whether the currency is enabled | [optional] 

## Example

```python
from openapi_client.models.currency_list_all_of import CurrencyListAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyListAllOf from a JSON string
currency_list_all_of_instance = CurrencyListAllOf.from_json(json)
# print the JSON string representation of the object
print CurrencyListAllOf.to_json()

# convert the object into a dict
currency_list_all_of_dict = currency_list_all_of_instance.to_dict()
# create an instance of CurrencyListAllOf from a dict
currency_list_all_of_form_dict = currency_list_all_of.from_dict(currency_list_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


