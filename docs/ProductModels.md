# ProductModels


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**ProductModelsEmbedded**](ProductModelsEmbedded.md) |  | [optional] 
**links** | [**ProductsLinks**](ProductsLinks.md) |  | [optional] 
**current_page** | **int** | Current page number | [optional] 

## Example

```python
from openapi_client.models.product_models import ProductModels

# TODO update the JSON string below
json = "{}"
# create an instance of ProductModels from a JSON string
product_models_instance = ProductModels.from_json(json)
# print the JSON string representation of the object
print ProductModels.to_json()

# convert the object into a dict
product_models_dict = product_models_instance.to_dict()
# create an instance of ProductModels from a dict
product_models_form_dict = product_models.from_dict(product_models_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


