# ProductModelListAllOfAssociations

Several associations related to groups, product and/or other product models, grouped by association types

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**association_type_code** | [**Dict[str, ProductListAllOf1AssociationsAssociationTypeCode]**](ProductListAllOf1AssociationsAssociationTypeCode.md) |  | [optional] 

## Example

```python
from akeneo.models.product_model_list_all_of_associations import ProductModelListAllOfAssociations

# TODO update the JSON string below
json = "{}"
# create an instance of ProductModelListAllOfAssociations from a JSON string
product_model_list_all_of_associations_instance = ProductModelListAllOfAssociations.from_json(json)
# print the JSON string representation of the object
print ProductModelListAllOfAssociations.to_json()

# convert the object into a dict
product_model_list_all_of_associations_dict = product_model_list_all_of_associations_instance.to_dict()
# create an instance of ProductModelListAllOfAssociations from a dict
product_model_list_all_of_associations_form_dict = product_model_list_all_of_associations.from_dict(product_model_list_all_of_associations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


