# Locales


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**LocalesEmbedded**](LocalesEmbedded.md) |  | [optional] 
**links** | [**ProductsLinks**](ProductsLinks.md) |  | [optional] 
**current_page** | **int** | Current page number | [optional] 

## Example

```python
from akeneo.models.locales import Locales

# TODO update the JSON string below
json = "{}"
# create an instance of Locales from a JSON string
locales_instance = Locales.from_json(json)
# print the JSON string representation of the object
print Locales.to_json()

# convert the object into a dict
locales_dict = locales_instance.to_dict()
# create an instance of Locales from a dict
locales_form_dict = locales.from_dict(locales_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


