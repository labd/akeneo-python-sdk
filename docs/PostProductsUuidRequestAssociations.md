# PostProductsUuidRequestAssociations

Several associations related to groups, product models and/or other products, grouped by association types

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**association_type_code** | [**PostProductsUuidRequestAssociationsAssociationTypeCode**](PostProductsUuidRequestAssociationsAssociationTypeCode.md) |  | [optional] 

## Example

```python
from akeneo.models.post_products_uuid_request_associations import PostProductsUuidRequestAssociations

# TODO update the JSON string below
json = "{}"
# create an instance of PostProductsUuidRequestAssociations from a JSON string
post_products_uuid_request_associations_instance = PostProductsUuidRequestAssociations.from_json(json)
# print the JSON string representation of the object
print PostProductsUuidRequestAssociations.to_json()

# convert the object into a dict
post_products_uuid_request_associations_dict = post_products_uuid_request_associations_instance.to_dict()
# create an instance of PostProductsUuidRequestAssociations from a dict
post_products_uuid_request_associations_form_dict = post_products_uuid_request_associations.from_dict(post_products_uuid_request_associations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


