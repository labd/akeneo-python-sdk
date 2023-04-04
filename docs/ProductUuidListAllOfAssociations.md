# ProductUuidListAllOfAssociations

Several associations related to groups, product models and/or other products, grouped by association types

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**association_type_code** | [**ProductUuidListAllOfAssociationsAssociationTypeCode**](ProductUuidListAllOfAssociationsAssociationTypeCode.md) |  | [optional] 

## Example

```python
from akeneo.models.product_uuid_list_all_of_associations import ProductUuidListAllOfAssociations

# TODO update the JSON string below
json = "{}"
# create an instance of ProductUuidListAllOfAssociations from a JSON string
product_uuid_list_all_of_associations_instance = ProductUuidListAllOfAssociations.from_json(json)
# print the JSON string representation of the object
print ProductUuidListAllOfAssociations.to_json()

# convert the object into a dict
product_uuid_list_all_of_associations_dict = product_uuid_list_all_of_associations_instance.to_dict()
# create an instance of ProductUuidListAllOfAssociations from a dict
product_uuid_list_all_of_associations_form_dict = product_uuid_list_all_of_associations.from_dict(product_uuid_list_all_of_associations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


