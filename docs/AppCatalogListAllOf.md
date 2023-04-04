# AppCatalogListAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Catalog id | [optional] 
**name** | **str** | Catalog name | [optional] 
**enabled** | **bool** | Whether the catalog is enabled or not | [optional] [default to False]

## Example

```python
from akeneo.models.app_catalog_list_all_of import AppCatalogListAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of AppCatalogListAllOf from a JSON string
app_catalog_list_all_of_instance = AppCatalogListAllOf.from_json(json)
# print the JSON string representation of the object
print AppCatalogListAllOf.to_json()

# convert the object into a dict
app_catalog_list_all_of_dict = app_catalog_list_all_of_instance.to_dict()
# create an instance of AppCatalogListAllOf from a dict
app_catalog_list_all_of_form_dict = app_catalog_list_all_of.from_dict(app_catalog_list_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


