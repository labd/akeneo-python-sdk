# Catalogs


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**CatalogsEmbedded**](CatalogsEmbedded.md) |  | [optional] 
**links** | [**ProductsLinks**](ProductsLinks.md) |  | [optional] 
**current_page** | **int** | Current page number | [optional] 

## Example

```python
from akeneo.models.catalogs import Catalogs

# TODO update the JSON string below
json = "{}"
# create an instance of Catalogs from a JSON string
catalogs_instance = Catalogs.from_json(json)
# print the JSON string representation of the object
print Catalogs.to_json()

# convert the object into a dict
catalogs_dict = catalogs_instance.to_dict()
# create an instance of Catalogs from a dict
catalogs_form_dict = catalogs.from_dict(catalogs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


