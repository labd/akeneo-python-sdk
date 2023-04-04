# GetPublishedProductsCode200ResponseAssociationsAssociationTypeCode


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | **List[str]** | Array of groups codes with which the published product is in relation | [optional] 
**products** | **List[str]** | Array of published product identifiers with which the published product is in relation | [optional] 
**product_models** | **List[str]** | Array of product model codes with which the product is in relation (only available since the v2.1) | [optional] 

## Example

```python
from akeneo.models.get_published_products_code200_response_associations_association_type_code import GetPublishedProductsCode200ResponseAssociationsAssociationTypeCode

# TODO update the JSON string below
json = "{}"
# create an instance of GetPublishedProductsCode200ResponseAssociationsAssociationTypeCode from a JSON string
get_published_products_code200_response_associations_association_type_code_instance = GetPublishedProductsCode200ResponseAssociationsAssociationTypeCode.from_json(json)
# print the JSON string representation of the object
print GetPublishedProductsCode200ResponseAssociationsAssociationTypeCode.to_json()

# convert the object into a dict
get_published_products_code200_response_associations_association_type_code_dict = get_published_products_code200_response_associations_association_type_code_instance.to_dict()
# create an instance of GetPublishedProductsCode200ResponseAssociationsAssociationTypeCode from a dict
get_published_products_code200_response_associations_association_type_code_form_dict = get_published_products_code200_response_associations_association_type_code.from_dict(get_published_products_code200_response_associations_association_type_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


