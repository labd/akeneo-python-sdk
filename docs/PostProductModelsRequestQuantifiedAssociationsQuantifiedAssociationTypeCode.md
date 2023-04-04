# PostProductModelsRequestQuantifiedAssociationsQuantifiedAssociationTypeCode


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | [**List[PostProductsRequestQuantifiedAssociationsQuantifiedAssociationTypeCodeProductsInner]**](PostProductsRequestQuantifiedAssociationsQuantifiedAssociationTypeCodeProductsInner.md) | Array of objects containing product identifiers and quantities with which the product model is in relation | [optional] 
**product_models** | [**List[PostProductsRequestQuantifiedAssociationsQuantifiedAssociationTypeCodeProductModelsInner]**](PostProductsRequestQuantifiedAssociationsQuantifiedAssociationTypeCodeProductModelsInner.md) | Array of objects containing product model codes and quantities with which the product model is in relation | [optional] 

## Example

```python
from openapi_client.models.post_product_models_request_quantified_associations_quantified_association_type_code import PostProductModelsRequestQuantifiedAssociationsQuantifiedAssociationTypeCode

# TODO update the JSON string below
json = "{}"
# create an instance of PostProductModelsRequestQuantifiedAssociationsQuantifiedAssociationTypeCode from a JSON string
post_product_models_request_quantified_associations_quantified_association_type_code_instance = PostProductModelsRequestQuantifiedAssociationsQuantifiedAssociationTypeCode.from_json(json)
# print the JSON string representation of the object
print PostProductModelsRequestQuantifiedAssociationsQuantifiedAssociationTypeCode.to_json()

# convert the object into a dict
post_product_models_request_quantified_associations_quantified_association_type_code_dict = post_product_models_request_quantified_associations_quantified_association_type_code_instance.to_dict()
# create an instance of PostProductModelsRequestQuantifiedAssociationsQuantifiedAssociationTypeCode from a dict
post_product_models_request_quantified_associations_quantified_association_type_code_form_dict = post_product_models_request_quantified_associations_quantified_association_type_code.from_dict(post_product_models_request_quantified_associations_quantified_association_type_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


