# FamilyVariantsEmbeddedItemsInnerAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Family variant code | 
**variant_attribute_sets** | [**List[FamilyVariantsEmbeddedItemsInnerAllOfVariantAttributeSetsInner]**](FamilyVariantsEmbeddedItemsInnerAllOfVariantAttributeSetsInner.md) | Attributes distribution according to the enrichment level | 
**labels** | [**FamilyVariantsEmbeddedItemsInnerAllOfLabels**](FamilyVariantsEmbeddedItemsInnerAllOfLabels.md) |  | [optional] 

## Example

```python
from akeneo.models.family_variants_embedded_items_inner_all_of import FamilyVariantsEmbeddedItemsInnerAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of FamilyVariantsEmbeddedItemsInnerAllOf from a JSON string
family_variants_embedded_items_inner_all_of_instance = FamilyVariantsEmbeddedItemsInnerAllOf.from_json(json)
# print the JSON string representation of the object
print FamilyVariantsEmbeddedItemsInnerAllOf.to_json()

# convert the object into a dict
family_variants_embedded_items_inner_all_of_dict = family_variants_embedded_items_inner_all_of_instance.to_dict()
# create an instance of FamilyVariantsEmbeddedItemsInnerAllOf from a dict
family_variants_embedded_items_inner_all_of_form_dict = family_variants_embedded_items_inner_all_of.from_dict(family_variants_embedded_items_inner_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


