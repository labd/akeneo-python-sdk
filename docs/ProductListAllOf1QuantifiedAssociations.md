# ProductListAllOf1QuantifiedAssociations

Several quantified associations related to products and/or product models, grouped by quantified association types (only available since the 5.0)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantified_association_type_code** | [**ProductListAllOf1QuantifiedAssociationsQuantifiedAssociationTypeCode**](ProductListAllOf1QuantifiedAssociationsQuantifiedAssociationTypeCode.md) |  | [optional] 

## Example

```python
from akeneo.models.product_list_all_of1_quantified_associations import ProductListAllOf1QuantifiedAssociations

# TODO update the JSON string below
json = "{}"
# create an instance of ProductListAllOf1QuantifiedAssociations from a JSON string
product_list_all_of1_quantified_associations_instance = ProductListAllOf1QuantifiedAssociations.from_json(json)
# print the JSON string representation of the object
print ProductListAllOf1QuantifiedAssociations.to_json()

# convert the object into a dict
product_list_all_of1_quantified_associations_dict = product_list_all_of1_quantified_associations_instance.to_dict()
# create an instance of ProductListAllOf1QuantifiedAssociations from a dict
product_list_all_of1_quantified_associations_form_dict = product_list_all_of1_quantified_associations.from_dict(product_list_all_of1_quantified_associations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


