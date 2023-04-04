# PostProductsRequestQuantifiedAssociations

Several quantified associations related to products and/or product models, grouped by quantified association types (only available since the 5.0)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantified_association_type_code** | [**PostProductsRequestQuantifiedAssociationsQuantifiedAssociationTypeCode**](PostProductsRequestQuantifiedAssociationsQuantifiedAssociationTypeCode.md) |  | [optional] 

## Example

```python
from openapi_client.models.post_products_request_quantified_associations import PostProductsRequestQuantifiedAssociations

# TODO update the JSON string below
json = "{}"
# create an instance of PostProductsRequestQuantifiedAssociations from a JSON string
post_products_request_quantified_associations_instance = PostProductsRequestQuantifiedAssociations.from_json(json)
# print the JSON string representation of the object
print PostProductsRequestQuantifiedAssociations.to_json()

# convert the object into a dict
post_products_request_quantified_associations_dict = post_products_request_quantified_associations_instance.to_dict()
# create an instance of PostProductsRequestQuantifiedAssociations from a dict
post_products_request_quantified_associations_form_dict = post_products_request_quantified_associations.from_dict(post_products_request_quantified_associations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


