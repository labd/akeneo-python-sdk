# PostProductModelsRequestAssociations

Several associations related to groups, product and/or other product models, grouped by association types

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**association_type_code** | [**PostProductsRequestAssociationsAssociationTypeCode**](PostProductsRequestAssociationsAssociationTypeCode.md) |  | [optional] 

## Example

```python
from openapi_client.models.post_product_models_request_associations import PostProductModelsRequestAssociations

# TODO update the JSON string below
json = "{}"
# create an instance of PostProductModelsRequestAssociations from a JSON string
post_product_models_request_associations_instance = PostProductModelsRequestAssociations.from_json(json)
# print the JSON string representation of the object
print PostProductModelsRequestAssociations.to_json()

# convert the object into a dict
post_product_models_request_associations_dict = post_product_models_request_associations_instance.to_dict()
# create an instance of PostProductModelsRequestAssociations from a dict
post_product_models_request_associations_form_dict = post_product_models_request_associations.from_dict(post_product_models_request_associations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


