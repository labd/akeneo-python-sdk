# AssociationTypesEmbeddedItemsInnerAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Association type code | 
**labels** | [**AssociationTypesEmbeddedItemsInnerAllOfLabels**](AssociationTypesEmbeddedItemsInnerAllOfLabels.md) |  | [optional] 
**is_quantified** | **bool** | When true, the association is a quantified association (Only available in the PIM Serenity version.) | [optional] [default to False]
**is_two_way** | **bool** | When true, the association is a two-way association (Only available in the PIM Serenity version.) | [optional] [default to False]

## Example

```python
from akeneo.models.association_types_embedded_items_inner_all_of import AssociationTypesEmbeddedItemsInnerAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationTypesEmbeddedItemsInnerAllOf from a JSON string
association_types_embedded_items_inner_all_of_instance = AssociationTypesEmbeddedItemsInnerAllOf.from_json(json)
# print the JSON string representation of the object
print AssociationTypesEmbeddedItemsInnerAllOf.to_json()

# convert the object into a dict
association_types_embedded_items_inner_all_of_dict = association_types_embedded_items_inner_all_of_instance.to_dict()
# create an instance of AssociationTypesEmbeddedItemsInnerAllOf from a dict
association_types_embedded_items_inner_all_of_form_dict = association_types_embedded_items_inner_all_of.from_dict(association_types_embedded_items_inner_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


