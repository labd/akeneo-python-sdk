# FamiliesEmbeddedItemsInnerAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Family code | 
**attribute_as_label** | **str** | Attribute code used as label | 
**attribute_as_image** | **str** | Attribute code used as the main picture in the user interface (only since v2.0) | [optional] [default to 'null']
**attributes** | **List[str]** | Attributes codes that compose the family | [optional] 
**attribute_requirements** | [**FamiliesEmbeddedItemsInnerAllOfAttributeRequirements**](FamiliesEmbeddedItemsInnerAllOfAttributeRequirements.md) |  | [optional] 
**labels** | [**FamiliesEmbeddedItemsInnerAllOfLabels**](FamiliesEmbeddedItemsInnerAllOfLabels.md) |  | [optional] 

## Example

```python
from akeneo.models.families_embedded_items_inner_all_of import FamiliesEmbeddedItemsInnerAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of FamiliesEmbeddedItemsInnerAllOf from a JSON string
families_embedded_items_inner_all_of_instance = FamiliesEmbeddedItemsInnerAllOf.from_json(json)
# print the JSON string representation of the object
print FamiliesEmbeddedItemsInnerAllOf.to_json()

# convert the object into a dict
families_embedded_items_inner_all_of_dict = families_embedded_items_inner_all_of_instance.to_dict()
# create an instance of FamiliesEmbeddedItemsInnerAllOf from a dict
families_embedded_items_inner_all_of_form_dict = families_embedded_items_inner_all_of.from_dict(families_embedded_items_inner_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


