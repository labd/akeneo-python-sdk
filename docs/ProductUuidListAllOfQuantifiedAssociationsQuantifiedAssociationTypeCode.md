# ProductUuidListAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | [**List[ProductUuidListAllOfQuantifiedAssociationsQuantifiedAssociationTypeCodeProducts]**](ProductUuidListAllOfQuantifiedAssociationsQuantifiedAssociationTypeCodeProducts.md) | Array of objects containing product uuids and quantities with which the product is in relation | [optional] 
**product_models** | [**List[ProductListAllOf1QuantifiedAssociationsQuantifiedAssociationTypeCodeProductModels]**](ProductListAllOf1QuantifiedAssociationsQuantifiedAssociationTypeCodeProductModels.md) | Array of objects containing product model codes and quantities with which the product is in relation | [optional] 

## Example

```python
from openapi_client.models.product_uuid_list_all_of_quantified_associations_quantified_association_type_code import ProductUuidListAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode

# TODO update the JSON string below
json = "{}"
# create an instance of ProductUuidListAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode from a JSON string
product_uuid_list_all_of_quantified_associations_quantified_association_type_code_instance = ProductUuidListAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode.from_json(json)
# print the JSON string representation of the object
print ProductUuidListAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode.to_json()

# convert the object into a dict
product_uuid_list_all_of_quantified_associations_quantified_association_type_code_dict = product_uuid_list_all_of_quantified_associations_quantified_association_type_code_instance.to_dict()
# create an instance of ProductUuidListAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode from a dict
product_uuid_list_all_of_quantified_associations_quantified_association_type_code_form_dict = product_uuid_list_all_of_quantified_associations_quantified_association_type_code.from_dict(product_uuid_list_all_of_quantified_associations_quantified_association_type_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


