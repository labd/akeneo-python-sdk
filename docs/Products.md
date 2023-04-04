# Products


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**ProductsEmbedded**](ProductsEmbedded.md) |  | [optional] 
**links** | [**ProductsLinks**](ProductsLinks.md) |  | [optional] 
**current_page** | **int** | Current page number | [optional] 

## Example

```python
from akeneo.models.products import Products

# TODO update the JSON string below
json = "{}"
# create an instance of Products from a JSON string
products_instance = Products.from_json(json)
# print the JSON string representation of the object
print Products.to_json()

# convert the object into a dict
products_dict = products_instance.to_dict()
# create an instance of Products from a dict
products_form_dict = products.from_dict(products_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


