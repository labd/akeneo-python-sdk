# PublishedProducts


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**PublishedProductsEmbedded**](PublishedProductsEmbedded.md) |  | [optional] 
**links** | [**ProductsLinks**](ProductsLinks.md) |  | [optional] 
**current_page** | **int** | Current page number | [optional] 

## Example

```python
from akeneo.models.published_products import PublishedProducts

# TODO update the JSON string below
json = "{}"
# create an instance of PublishedProducts from a JSON string
published_products_instance = PublishedProducts.from_json(json)
# print the JSON string representation of the object
print PublishedProducts.to_json()

# convert the object into a dict
published_products_dict = published_products_instance.to_dict()
# create an instance of PublishedProducts from a dict
published_products_form_dict = published_products.from_dict(published_products_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


