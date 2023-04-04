# LocaleListAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Locale code | 
**enabled** | **bool** | Whether the locale is enabled | [optional] [default to False]

## Example

```python
from akeneo.models.locale_list_all_of import LocaleListAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of LocaleListAllOf from a JSON string
locale_list_all_of_instance = LocaleListAllOf.from_json(json)
# print the JSON string representation of the object
print LocaleListAllOf.to_json()

# convert the object into a dict
locale_list_all_of_dict = locale_list_all_of_instance.to_dict()
# create an instance of LocaleListAllOf from a dict
locale_list_all_of_form_dict = locale_list_all_of.from_dict(locale_list_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


