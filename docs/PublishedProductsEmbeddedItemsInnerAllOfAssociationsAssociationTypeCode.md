# PublishedProductsEmbeddedItemsInnerAllOfAssociationsAssociationTypeCode


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | **List[str]** | Array of groups codes with which the published product is in relation | [optional] 
**products** | **List[str]** | Array of published product identifiers with which the published product is in relation | [optional] 
**product_models** | **List[str]** | Array of product model codes with which the product is in relation (only available since the v2.1) | [optional] 

## Example

```python
from akeneo.models.published_products_embedded_items_inner_all_of_associations_association_type_code import PublishedProductsEmbeddedItemsInnerAllOfAssociationsAssociationTypeCode

# TODO update the JSON string below
json = "{}"
# create an instance of PublishedProductsEmbeddedItemsInnerAllOfAssociationsAssociationTypeCode from a JSON string
published_products_embedded_items_inner_all_of_associations_association_type_code_instance = PublishedProductsEmbeddedItemsInnerAllOfAssociationsAssociationTypeCode.from_json(json)
# print the JSON string representation of the object
print PublishedProductsEmbeddedItemsInnerAllOfAssociationsAssociationTypeCode.to_json()

# convert the object into a dict
published_products_embedded_items_inner_all_of_associations_association_type_code_dict = published_products_embedded_items_inner_all_of_associations_association_type_code_instance.to_dict()
# create an instance of PublishedProductsEmbeddedItemsInnerAllOfAssociationsAssociationTypeCode from a dict
published_products_embedded_items_inner_all_of_associations_association_type_code_form_dict = published_products_embedded_items_inner_all_of_associations_association_type_code.from_dict(published_products_embedded_items_inner_all_of_associations_association_type_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


