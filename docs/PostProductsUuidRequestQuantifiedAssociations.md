# PostProductsUuidRequestQuantifiedAssociations

Several quantified associations related to products and/or product models, grouped by quantified association types (only available since the 5.0)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantified_association_type_code** | [**PostProductsUuidRequestQuantifiedAssociationsQuantifiedAssociationTypeCode**](PostProductsUuidRequestQuantifiedAssociationsQuantifiedAssociationTypeCode.md) |  | [optional] 

## Example

```python
from akeneo.models.post_products_uuid_request_quantified_associations import PostProductsUuidRequestQuantifiedAssociations

# TODO update the JSON string below
json = "{}"
# create an instance of PostProductsUuidRequestQuantifiedAssociations from a JSON string
post_products_uuid_request_quantified_associations_instance = PostProductsUuidRequestQuantifiedAssociations.from_json(json)
# print the JSON string representation of the object
print PostProductsUuidRequestQuantifiedAssociations.to_json()

# convert the object into a dict
post_products_uuid_request_quantified_associations_dict = post_products_uuid_request_quantified_associations_instance.to_dict()
# create an instance of PostProductsUuidRequestQuantifiedAssociations from a dict
post_products_uuid_request_quantified_associations_form_dict = post_products_uuid_request_quantified_associations.from_dict(post_products_uuid_request_quantified_associations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


