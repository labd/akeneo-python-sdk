# CatalogsEmbeddedItemsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ProductsEmbeddedItemsInnerAllOfLinks**](ProductsEmbeddedItemsInnerAllOfLinks.md) |  | [optional] 
**id** | **str** | Catalog id | [optional] 
**name** | **str** | Catalog name | [optional] 
**enabled** | **bool** | Whether the catalog is enabled or not | [optional] [default to False]

## Example

```python
from openapi_client.models.catalogs_embedded_items_inner import CatalogsEmbeddedItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogsEmbeddedItemsInner from a JSON string
catalogs_embedded_items_inner_instance = CatalogsEmbeddedItemsInner.from_json(json)
# print the JSON string representation of the object
print CatalogsEmbeddedItemsInner.to_json()

# convert the object into a dict
catalogs_embedded_items_inner_dict = catalogs_embedded_items_inner_instance.to_dict()
# create an instance of CatalogsEmbeddedItemsInner from a dict
catalogs_embedded_items_inner_form_dict = catalogs_embedded_items_inner.from_dict(catalogs_embedded_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


