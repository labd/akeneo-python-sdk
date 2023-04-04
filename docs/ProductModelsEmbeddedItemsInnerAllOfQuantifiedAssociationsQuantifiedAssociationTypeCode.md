# ProductModelsEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | [**List[ProductsEmbeddedItemsInnerAllOf1QuantifiedAssociationsQuantifiedAssociationTypeCodeProductsInner]**](ProductsEmbeddedItemsInnerAllOf1QuantifiedAssociationsQuantifiedAssociationTypeCodeProductsInner.md) | Array of objects containing product identifiers and quantities with which the product model is in relation | [optional] 
**product_models** | [**List[ProductsEmbeddedItemsInnerAllOf1QuantifiedAssociationsQuantifiedAssociationTypeCodeProductModelsInner]**](ProductsEmbeddedItemsInnerAllOf1QuantifiedAssociationsQuantifiedAssociationTypeCodeProductModelsInner.md) | Array of objects containing product model codes and quantities with which the product model is in relation | [optional] 

## Example

```python
from openapi_client.models.product_models_embedded_items_inner_all_of_quantified_associations_quantified_association_type_code import ProductModelsEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode

# TODO update the JSON string below
json = "{}"
# create an instance of ProductModelsEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode from a JSON string
product_models_embedded_items_inner_all_of_quantified_associations_quantified_association_type_code_instance = ProductModelsEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode.from_json(json)
# print the JSON string representation of the object
print ProductModelsEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode.to_json()

# convert the object into a dict
product_models_embedded_items_inner_all_of_quantified_associations_quantified_association_type_code_dict = product_models_embedded_items_inner_all_of_quantified_associations_quantified_association_type_code_instance.to_dict()
# create an instance of ProductModelsEmbeddedItemsInnerAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode from a dict
product_models_embedded_items_inner_all_of_quantified_associations_quantified_association_type_code_form_dict = product_models_embedded_items_inner_all_of_quantified_associations_quantified_association_type_code.from_dict(product_models_embedded_items_inner_all_of_quantified_associations_quantified_association_type_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


