# FamiliesEmbeddedItemsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ProductsEmbeddedItemsInnerAllOfLinks**](ProductsEmbeddedItemsInnerAllOfLinks.md) |  | [optional] 
**code** | **str** | Family code | 
**attribute_as_label** | **str** | Attribute code used as label | 
**attribute_as_image** | **str** | Attribute code used as the main picture in the user interface (only since v2.0) | [optional] [default to 'null']
**attributes** | **List[str]** | Attributes codes that compose the family | [optional] 
**attribute_requirements** | [**FamiliesEmbeddedItemsInnerAllOfAttributeRequirements**](FamiliesEmbeddedItemsInnerAllOfAttributeRequirements.md) |  | [optional] 
**labels** | [**FamiliesEmbeddedItemsInnerAllOfLabels**](FamiliesEmbeddedItemsInnerAllOfLabels.md) |  | [optional] 

## Example

```python
from akeneo.models.families_embedded_items_inner import FamiliesEmbeddedItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of FamiliesEmbeddedItemsInner from a JSON string
families_embedded_items_inner_instance = FamiliesEmbeddedItemsInner.from_json(json)
# print the JSON string representation of the object
print FamiliesEmbeddedItemsInner.to_json()

# convert the object into a dict
families_embedded_items_inner_dict = families_embedded_items_inner_instance.to_dict()
# create an instance of FamiliesEmbeddedItemsInner from a dict
families_embedded_items_inner_form_dict = families_embedded_items_inner.from_dict(families_embedded_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


