# LocalesEmbeddedItemsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ProductsEmbeddedItemsInnerAllOfLinks**](ProductsEmbeddedItemsInnerAllOfLinks.md) |  | [optional] 
**code** | **str** | Locale code | 
**enabled** | **bool** | Whether the locale is enabled | [optional] [default to False]

## Example

```python
from akeneo.models.locales_embedded_items_inner import LocalesEmbeddedItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of LocalesEmbeddedItemsInner from a JSON string
locales_embedded_items_inner_instance = LocalesEmbeddedItemsInner.from_json(json)
# print the JSON string representation of the object
print LocalesEmbeddedItemsInner.to_json()

# convert the object into a dict
locales_embedded_items_inner_dict = locales_embedded_items_inner_instance.to_dict()
# create an instance of LocalesEmbeddedItemsInner from a dict
locales_embedded_items_inner_form_dict = locales_embedded_items_inner.from_dict(locales_embedded_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


