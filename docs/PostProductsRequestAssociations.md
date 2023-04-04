# PostProductsRequestAssociations

Several associations related to groups, product models and/or other products, grouped by association types

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**association_type_code** | [**PostProductsRequestAssociationsAssociationTypeCode**](PostProductsRequestAssociationsAssociationTypeCode.md) |  | [optional] 

## Example

```python
from akeneo.models.post_products_request_associations import PostProductsRequestAssociations

# TODO update the JSON string below
json = "{}"
# create an instance of PostProductsRequestAssociations from a JSON string
post_products_request_associations_instance = PostProductsRequestAssociations.from_json(json)
# print the JSON string representation of the object
print PostProductsRequestAssociations.to_json()

# convert the object into a dict
post_products_request_associations_dict = post_products_request_associations_instance.to_dict()
# create an instance of PostProductsRequestAssociations from a dict
post_products_request_associations_form_dict = post_products_request_associations.from_dict(post_products_request_associations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


