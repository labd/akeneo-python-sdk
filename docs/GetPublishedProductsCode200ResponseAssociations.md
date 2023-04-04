# GetPublishedProductsCode200ResponseAssociations

Several associations related to groups and/or other published products, grouped by association types

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**association_type_code** | [**GetPublishedProductsCode200ResponseAssociationsAssociationTypeCode**](GetPublishedProductsCode200ResponseAssociationsAssociationTypeCode.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_published_products_code200_response_associations import GetPublishedProductsCode200ResponseAssociations

# TODO update the JSON string below
json = "{}"
# create an instance of GetPublishedProductsCode200ResponseAssociations from a JSON string
get_published_products_code200_response_associations_instance = GetPublishedProductsCode200ResponseAssociations.from_json(json)
# print the JSON string representation of the object
print GetPublishedProductsCode200ResponseAssociations.to_json()

# convert the object into a dict
get_published_products_code200_response_associations_dict = get_published_products_code200_response_associations_instance.to_dict()
# create an instance of GetPublishedProductsCode200ResponseAssociations from a dict
get_published_products_code200_response_associations_form_dict = get_published_products_code200_response_associations.from_dict(get_published_products_code200_response_associations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


