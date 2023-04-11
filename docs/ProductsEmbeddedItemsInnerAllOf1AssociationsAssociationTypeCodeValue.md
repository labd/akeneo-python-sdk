# ProductsEmbeddedItemsInnerAllOf1AssociationsAssociationTypeCodeValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | **List[str]** | Array of groups codes with which the product is in relation | [optional] 
**products** | **List[str]** | Array of product identifiers with which the product is in relation | [optional] 
**product_models** | **List[str]** | Array of product model codes with which the product is in relation (only available since the v2.1) | [optional] 

## Example

```python
from akeneo.models.products_embedded_items_inner_all_of1_associations_association_type_code_value import ProductsEmbeddedItemsInnerAllOf1AssociationsAssociationTypeCodeValue

# TODO update the JSON string below
json = "{}"
# create an instance of ProductsEmbeddedItemsInnerAllOf1AssociationsAssociationTypeCodeValue from a JSON string
products_embedded_items_inner_all_of1_associations_association_type_code_value_instance = ProductsEmbeddedItemsInnerAllOf1AssociationsAssociationTypeCodeValue.from_json(json)
# print the JSON string representation of the object
print ProductsEmbeddedItemsInnerAllOf1AssociationsAssociationTypeCodeValue.to_json()

# convert the object into a dict
products_embedded_items_inner_all_of1_associations_association_type_code_value_dict = products_embedded_items_inner_all_of1_associations_association_type_code_value_instance.to_dict()
# create an instance of ProductsEmbeddedItemsInnerAllOf1AssociationsAssociationTypeCodeValue from a dict
products_embedded_items_inner_all_of1_associations_association_type_code_value_form_dict = products_embedded_items_inner_all_of1_associations_association_type_code_value.from_dict(products_embedded_items_inner_all_of1_associations_association_type_code_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


