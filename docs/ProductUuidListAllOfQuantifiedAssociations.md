# ProductUuidListAllOfQuantifiedAssociations

Several quantified associations related to products and/or product models, grouped by quantified association types (only available since the 5.0)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantified_association_type_code** | [**ProductUuidListAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode**](ProductUuidListAllOfQuantifiedAssociationsQuantifiedAssociationTypeCode.md) |  | [optional] 

## Example

```python
from akeneo.models.product_uuid_list_all_of_quantified_associations import ProductUuidListAllOfQuantifiedAssociations

# TODO update the JSON string below
json = "{}"
# create an instance of ProductUuidListAllOfQuantifiedAssociations from a JSON string
product_uuid_list_all_of_quantified_associations_instance = ProductUuidListAllOfQuantifiedAssociations.from_json(json)
# print the JSON string representation of the object
print ProductUuidListAllOfQuantifiedAssociations.to_json()

# convert the object into a dict
product_uuid_list_all_of_quantified_associations_dict = product_uuid_list_all_of_quantified_associations_instance.to_dict()
# create an instance of ProductUuidListAllOfQuantifiedAssociations from a dict
product_uuid_list_all_of_quantified_associations_form_dict = product_uuid_list_all_of_quantified_associations.from_dict(product_uuid_list_all_of_quantified_associations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


