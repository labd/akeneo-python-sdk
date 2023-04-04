# ProductModelListAllOfQuantifiedAssociations

Several quantified associations related to products and/or product models, grouped by quantified association types (only available since the 5.0)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantified_association_type_code** | [**ProductModelListAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode**](ProductModelListAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode.md) |  | [optional] 

## Example

```python
from akeneo.models.product_model_list_all_of_quantified_associations import ProductModelListAllOfQuantifiedAssociations

# TODO update the JSON string below
json = "{}"
# create an instance of ProductModelListAllOfQuantifiedAssociations from a JSON string
product_model_list_all_of_quantified_associations_instance = ProductModelListAllOfQuantifiedAssociations.from_json(json)
# print the JSON string representation of the object
print ProductModelListAllOfQuantifiedAssociations.to_json()

# convert the object into a dict
product_model_list_all_of_quantified_associations_dict = product_model_list_all_of_quantified_associations_instance.to_dict()
# create an instance of ProductModelListAllOfQuantifiedAssociations from a dict
product_model_list_all_of_quantified_associations_form_dict = product_model_list_all_of_quantified_associations.from_dict(product_model_list_all_of_quantified_associations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


