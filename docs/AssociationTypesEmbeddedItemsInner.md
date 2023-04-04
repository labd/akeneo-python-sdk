# AssociationTypesEmbeddedItemsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ProductsEmbeddedItemsInnerAllOfLinks**](ProductsEmbeddedItemsInnerAllOfLinks.md) |  | [optional] 
**code** | **str** | Association type code | 
**labels** | [**AssociationTypesEmbeddedItemsInnerAllOfLabels**](AssociationTypesEmbeddedItemsInnerAllOfLabels.md) |  | [optional] 
**is_quantified** | **bool** | When true, the association is a quantified association (Only available in the PIM Serenity version.) | [optional] [default to False]
**is_two_way** | **bool** | When true, the association is a two-way association (Only available in the PIM Serenity version.) | [optional] [default to False]

## Example

```python
from openapi_client.models.association_types_embedded_items_inner import AssociationTypesEmbeddedItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationTypesEmbeddedItemsInner from a JSON string
association_types_embedded_items_inner_instance = AssociationTypesEmbeddedItemsInner.from_json(json)
# print the JSON string representation of the object
print AssociationTypesEmbeddedItemsInner.to_json()

# convert the object into a dict
association_types_embedded_items_inner_dict = association_types_embedded_items_inner_instance.to_dict()
# create an instance of AssociationTypesEmbeddedItemsInner from a dict
association_types_embedded_items_inner_form_dict = association_types_embedded_items_inner.from_dict(association_types_embedded_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


