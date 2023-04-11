# ProductAssociations

Several associations related to groups, product models and/or other products, grouped by association types

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**association_type_code** | [**Dict[str, ProductsEmbeddedItemsInnerAllOf1AssociationsAssociationTypeCode]**](ProductsEmbeddedItemsInnerAllOf1AssociationsAssociationTypeCode.md) |  | [optional] 

## Example

```python
from akeneo.models.product_associations import ProductAssociations

# TODO update the JSON string below
json = "{}"
# create an instance of ProductAssociations from a JSON string
product_associations_instance = ProductAssociations.from_json(json)
# print the JSON string representation of the object
print ProductAssociations.to_json()

# convert the object into a dict
product_associations_dict = product_associations_instance.to_dict()
# create an instance of ProductAssociations from a dict
product_associations_form_dict = product_associations.from_dict(product_associations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


