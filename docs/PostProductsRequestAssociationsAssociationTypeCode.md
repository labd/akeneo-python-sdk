# PostProductsRequestAssociationsAssociationTypeCode


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | **List[str]** | Array of groups codes with which the product is in relation | [optional] 
**products** | **List[str]** | Array of product identifiers with which the product is in relation | [optional] 
**product_models** | **List[str]** | Array of product model codes with which the product is in relation (only available since the v2.1) | [optional] 

## Example

```python
from akeneo.models.post_products_request_associations_association_type_code import PostProductsRequestAssociationsAssociationTypeCode

# TODO update the JSON string below
json = "{}"
# create an instance of PostProductsRequestAssociationsAssociationTypeCode from a JSON string
post_products_request_associations_association_type_code_instance = PostProductsRequestAssociationsAssociationTypeCode.from_json(json)
# print the JSON string representation of the object
print PostProductsRequestAssociationsAssociationTypeCode.to_json()

# convert the object into a dict
post_products_request_associations_association_type_code_dict = post_products_request_associations_association_type_code_instance.to_dict()
# create an instance of PostProductsRequestAssociationsAssociationTypeCode from a dict
post_products_request_associations_association_type_code_form_dict = post_products_request_associations_association_type_code.from_dict(post_products_request_associations_association_type_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


