# ProductUuidAssociations

Several associations related to groups, product models and/or other products, grouped by association types

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**association_type_code** | [**ProductUuidAssociationsAssociationTypeCode**](ProductUuidAssociationsAssociationTypeCode.md) |  | [optional] 

## Example

```python
from akeneo.models.product_uuid_associations import ProductUuidAssociations

# TODO update the JSON string below
json = "{}"
# create an instance of ProductUuidAssociations from a JSON string
product_uuid_associations_instance = ProductUuidAssociations.from_json(json)
# print the JSON string representation of the object
print ProductUuidAssociations.to_json()

# convert the object into a dict
product_uuid_associations_dict = product_uuid_associations_instance.to_dict()
# create an instance of ProductUuidAssociations from a dict
product_uuid_associations_form_dict = product_uuid_associations.from_dict(product_uuid_associations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


