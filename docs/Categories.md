# Categories


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**CategoriesEmbedded**](CategoriesEmbedded.md) |  | [optional] 
**links** | [**ProductsLinks**](ProductsLinks.md) |  | [optional] 
**current_page** | **int** | Current page number | [optional] 

## Example

```python
from openapi_client.models.categories import Categories

# TODO update the JSON string below
json = "{}"
# create an instance of Categories from a JSON string
categories_instance = Categories.from_json(json)
# print the JSON string representation of the object
print Categories.to_json()

# convert the object into a dict
categories_dict = categories_instance.to_dict()
# create an instance of Categories from a dict
categories_form_dict = categories.from_dict(categories_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


