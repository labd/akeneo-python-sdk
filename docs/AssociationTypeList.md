# AssociationTypeList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ProductListAllOfLinks**](ProductListAllOfLinks.md) |  | [optional] 
**code** | **str** | Association type code | 
**labels** | [**AssociationTypeListAllOfLabels**](AssociationTypeListAllOfLabels.md) |  | [optional] 
**is_quantified** | **bool** | When true, the association is a quantified association (Only available in the PIM Serenity version.) | [optional] [default to False]
**is_two_way** | **bool** | When true, the association is a two-way association (Only available in the PIM Serenity version.) | [optional] [default to False]

## Example

```python
from openapi_client.models.association_type_list import AssociationTypeList

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationTypeList from a JSON string
association_type_list_instance = AssociationTypeList.from_json(json)
# print the JSON string representation of the object
print AssociationTypeList.to_json()

# convert the object into a dict
association_type_list_dict = association_type_list_instance.to_dict()
# create an instance of AssociationTypeList from a dict
association_type_list_form_dict = association_type_list.from_dict(association_type_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


