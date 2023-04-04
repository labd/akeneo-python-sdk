# ProductsEmbedded


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ProductsEmbeddedItemsInner]**](ProductsEmbeddedItemsInner.md) |  | [optional] 

## Example

```python
from akeneo.models.products_embedded import ProductsEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of ProductsEmbedded from a JSON string
products_embedded_instance = ProductsEmbedded.from_json(json)
# print the JSON string representation of the object
print ProductsEmbedded.to_json()

# convert the object into a dict
products_embedded_dict = products_embedded_instance.to_dict()
# create an instance of ProductsEmbedded from a dict
products_embedded_form_dict = products_embedded.from_dict(products_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


