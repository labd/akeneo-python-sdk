# LocaleList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ProductListAllOfLinks**](ProductListAllOfLinks.md) |  | [optional] 
**code** | **str** | Locale code | 
**enabled** | **bool** | Whether the locale is enabled | [optional] [default to False]

## Example

```python
from akeneo.models.locale_list import LocaleList

# TODO update the JSON string below
json = "{}"
# create an instance of LocaleList from a JSON string
locale_list_instance = LocaleList.from_json(json)
# print the JSON string representation of the object
print LocaleList.to_json()

# convert the object into a dict
locale_list_dict = locale_list_instance.to_dict()
# create an instance of LocaleList from a dict
locale_list_form_dict = locale_list.from_dict(locale_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


