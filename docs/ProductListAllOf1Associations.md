# ProductListAllOf1Associations

Several associations related to groups, product models and/or other products, grouped by association types

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**association_type_code** | [**Dict[str, ProductListAllOf1AssociationsAssociationTypeCode]**](ProductListAllOf1AssociationsAssociationTypeCode.md) |  | [optional] 

## Example

```python
from akeneo.models.product_list_all_of1_associations import ProductListAllOf1Associations

# TODO update the JSON string below
json = "{}"
# create an instance of ProductListAllOf1Associations from a JSON string
product_list_all_of1_associations_instance = ProductListAllOf1Associations.from_json(json)
# print the JSON string representation of the object
print ProductListAllOf1Associations.to_json()

# convert the object into a dict
product_list_all_of1_associations_dict = product_list_all_of1_associations_instance.to_dict()
# create an instance of ProductListAllOf1Associations from a dict
product_list_all_of1_associations_form_dict = product_list_all_of1_associations.from_dict(product_list_all_of1_associations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


