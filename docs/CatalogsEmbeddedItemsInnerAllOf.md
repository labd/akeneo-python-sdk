# CatalogsEmbeddedItemsInnerAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Catalog id | [optional] 
**name** | **str** | Catalog name | [optional] 
**enabled** | **bool** | Whether the catalog is enabled or not | [optional] [default to False]

## Example

```python
from akeneo.models.catalogs_embedded_items_inner_all_of import CatalogsEmbeddedItemsInnerAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogsEmbeddedItemsInnerAllOf from a JSON string
catalogs_embedded_items_inner_all_of_instance = CatalogsEmbeddedItemsInnerAllOf.from_json(json)
# print the JSON string representation of the object
print CatalogsEmbeddedItemsInnerAllOf.to_json()

# convert the object into a dict
catalogs_embedded_items_inner_all_of_dict = catalogs_embedded_items_inner_all_of_instance.to_dict()
# create an instance of CatalogsEmbeddedItemsInnerAllOf from a dict
catalogs_embedded_items_inner_all_of_form_dict = catalogs_embedded_items_inner_all_of.from_dict(catalogs_embedded_items_inner_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


