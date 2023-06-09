# GetAppCatalogsMappingSchemaProduct200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id of your schema | [optional] 
**var_schema** | **str** | $schema indicates which product mapping schema version your app uses | 
**comment** | **str** | allows you to add a comment | [optional] 
**title** | **str** | allows you to add a title to your mapping schema | [optional] 
**description** | **str** | allows you to add a description of your mapping schema | [optional] 
**type** | **str** | should always be \&quot;object\&quot; | [optional] 
**properties** | **object** | list and describe the targets your app expects | 

## Example

```python
from akeneo.models.get_app_catalogs_mapping_schema_product200_response import GetAppCatalogsMappingSchemaProduct200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAppCatalogsMappingSchemaProduct200Response from a JSON string
get_app_catalogs_mapping_schema_product200_response_instance = GetAppCatalogsMappingSchemaProduct200Response.from_json(json)
# print the JSON string representation of the object
print GetAppCatalogsMappingSchemaProduct200Response.to_json()

# convert the object into a dict
get_app_catalogs_mapping_schema_product200_response_dict = get_app_catalogs_mapping_schema_product200_response_instance.to_dict()
# create an instance of GetAppCatalogsMappingSchemaProduct200Response from a dict
get_app_catalogs_mapping_schema_product200_response_form_dict = get_app_catalogs_mapping_schema_product200_response.from_dict(get_app_catalogs_mapping_schema_product200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


