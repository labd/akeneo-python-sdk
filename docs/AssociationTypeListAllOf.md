# AssociationTypeListAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Association type code | 
**labels** | [**AssociationTypeListAllOfLabels**](AssociationTypeListAllOfLabels.md) |  | [optional] 
**is_quantified** | **bool** | When true, the association is a quantified association (Only available in the PIM Serenity version.) | [optional] [default to False]
**is_two_way** | **bool** | When true, the association is a two-way association (Only available in the PIM Serenity version.) | [optional] [default to False]

## Example

```python
from openapi_client.models.association_type_list_all_of import AssociationTypeListAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationTypeListAllOf from a JSON string
association_type_list_all_of_instance = AssociationTypeListAllOf.from_json(json)
# print the JSON string representation of the object
print AssociationTypeListAllOf.to_json()

# convert the object into a dict
association_type_list_all_of_dict = association_type_list_all_of_instance.to_dict()
# create an instance of AssociationTypeListAllOf from a dict
association_type_list_all_of_form_dict = association_type_list_all_of.from_dict(association_type_list_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


