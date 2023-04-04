# CategoriesEmbedded


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CategoriesEmbeddedItemsInner]**](CategoriesEmbeddedItemsInner.md) |  | [optional] 

## Example

```python
from akeneo.models.categories_embedded import CategoriesEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of CategoriesEmbedded from a JSON string
categories_embedded_instance = CategoriesEmbedded.from_json(json)
# print the JSON string representation of the object
print CategoriesEmbedded.to_json()

# convert the object into a dict
categories_embedded_dict = categories_embedded_instance.to_dict()
# create an instance of CategoriesEmbedded from a dict
categories_embedded_form_dict = categories_embedded.from_dict(categories_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


