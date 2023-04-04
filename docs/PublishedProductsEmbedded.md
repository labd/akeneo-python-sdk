# PublishedProductsEmbedded


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PublishedProductsEmbeddedItemsInner]**](PublishedProductsEmbeddedItemsInner.md) |  | [optional] 

## Example

```python
from akeneo.models.published_products_embedded import PublishedProductsEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of PublishedProductsEmbedded from a JSON string
published_products_embedded_instance = PublishedProductsEmbedded.from_json(json)
# print the JSON string representation of the object
print PublishedProductsEmbedded.to_json()

# convert the object into a dict
published_products_embedded_dict = published_products_embedded_instance.to_dict()
# create an instance of PublishedProductsEmbedded from a dict
published_products_embedded_form_dict = published_products_embedded.from_dict(published_products_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


