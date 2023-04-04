# FamilyVariant


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Family variant code | 
**variant_attribute_sets** | [**List[FamilyVariantsEmbeddedItemsInnerAllOfVariantAttributeSetsInner]**](FamilyVariantsEmbeddedItemsInnerAllOfVariantAttributeSetsInner.md) | Attributes distribution according to the enrichment level | 
**labels** | [**FamilyVariantsEmbeddedItemsInnerAllOfLabels**](FamilyVariantsEmbeddedItemsInnerAllOfLabels.md) |  | [optional] 

## Example

```python
from akeneo.models.family_variant import FamilyVariant

# TODO update the JSON string below
json = "{}"
# create an instance of FamilyVariant from a JSON string
family_variant_instance = FamilyVariant.from_json(json)
# print the JSON string representation of the object
print FamilyVariant.to_json()

# convert the object into a dict
family_variant_dict = family_variant_instance.to_dict()
# create an instance of FamilyVariant from a dict
family_variant_form_dict = family_variant.from_dict(family_variant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


