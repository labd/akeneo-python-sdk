# ProductModelsEmbedded


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ProductModelsEmbeddedItemsInner]**](ProductModelsEmbeddedItemsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.product_models_embedded import ProductModelsEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of ProductModelsEmbedded from a JSON string
product_models_embedded_instance = ProductModelsEmbedded.from_json(json)
# print the JSON string representation of the object
print ProductModelsEmbedded.to_json()

# convert the object into a dict
product_models_embedded_dict = product_models_embedded_instance.to_dict()
# create an instance of ProductModelsEmbedded from a dict
product_models_embedded_form_dict = product_models_embedded.from_dict(product_models_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


