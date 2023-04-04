# Products1EmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | [**List[Products1EmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCodeProductsInner]**](Products1EmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCodeProductsInner.md) | Array of objects containing product uuids and quantities with which the product is in relation | [optional] 
**product_models** | [**List[ProductsEmbeddedItemsInnerAllOf1QuantifiedAssociationsQuantifiedAssociationTypeCodeProductModelsInner]**](ProductsEmbeddedItemsInnerAllOf1QuantifiedAssociationsQuantifiedAssociationTypeCodeProductModelsInner.md) | Array of objects containing product model codes and quantities with which the product is in relation | [optional] 

## Example

```python
from akeneo.models.products1_embedded_items_inner_all_of_quantified_associations_quantified_association_type_code import Products1EmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode

# TODO update the JSON string below
json = "{}"
# create an instance of Products1EmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode from a JSON string
products1_embedded_items_inner_all_of_quantified_associations_quantified_association_type_code_instance = Products1EmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode.from_json(json)
# print the JSON string representation of the object
print Products1EmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode.to_json()

# convert the object into a dict
products1_embedded_items_inner_all_of_quantified_associations_quantified_association_type_code_dict = products1_embedded_items_inner_all_of_quantified_associations_quantified_association_type_code_instance.to_dict()
# create an instance of Products1EmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode from a dict
products1_embedded_items_inner_all_of_quantified_associations_quantified_association_type_code_form_dict = products1_embedded_items_inner_all_of_quantified_associations_quantified_association_type_code.from_dict(products1_embedded_items_inner_all_of_quantified_associations_quantified_association_type_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


