# ProductListAllOf1AssociationsAssociationTypeCode


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | **List[str]** | Array of groups codes with which the product is in relation | [optional] 
**products** | **List[str]** | Array of product identifiers with which the product is in relation | [optional] 
**product_models** | **List[str]** | Array of product model codes with which the product is in relation (only available since the v2.1) | [optional] 

## Example

```python
from akeneo.models.product_list_all_of1_associations_association_type_code import ProductListAllOf1AssociationsAssociationTypeCode

# TODO update the JSON string below
json = "{}"
# create an instance of ProductListAllOf1AssociationsAssociationTypeCode from a JSON string
product_list_all_of1_associations_association_type_code_instance = ProductListAllOf1AssociationsAssociationTypeCode.from_json(json)
# print the JSON string representation of the object
print ProductListAllOf1AssociationsAssociationTypeCode.to_json()

# convert the object into a dict
product_list_all_of1_associations_association_type_code_dict = product_list_all_of1_associations_association_type_code_instance.to_dict()
# create an instance of ProductListAllOf1AssociationsAssociationTypeCode from a dict
product_list_all_of1_associations_association_type_code_form_dict = product_list_all_of1_associations_association_type_code.from_dict(product_list_all_of1_associations_association_type_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


