# AssociationType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Association type code | 
**labels** | [**AssociationTypesEmbeddedItemsInnerAllOfLabels**](AssociationTypesEmbeddedItemsInnerAllOfLabels.md) |  | [optional] 
**is_quantified** | **bool** | When true, the association is a quantified association (Only available in the PIM Serenity version.) | [optional] [default to False]
**is_two_way** | **bool** | When true, the association is a two-way association (Only available in the PIM Serenity version.) | [optional] [default to False]

## Example

```python
from akeneo.models.association_type import AssociationType

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationType from a JSON string
association_type_instance = AssociationType.from_json(json)
# print the JSON string representation of the object
print AssociationType.to_json()

# convert the object into a dict
association_type_dict = association_type_instance.to_dict()
# create an instance of AssociationType from a dict
association_type_form_dict = association_type.from_dict(association_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


