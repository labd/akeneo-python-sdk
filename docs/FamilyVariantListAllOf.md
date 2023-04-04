# FamilyVariantListAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Family variant code | 
**variant_attribute_sets** | [**List[FamilyVariantListAllOfVariantAttributeSets]**](FamilyVariantListAllOfVariantAttributeSets.md) | Attributes distribution according to the enrichment level | 
**labels** | [**FamilyVariantListAllOfLabels**](FamilyVariantListAllOfLabels.md) |  | [optional] 

## Example

```python
from akeneo.models.family_variant_list_all_of import FamilyVariantListAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of FamilyVariantListAllOf from a JSON string
family_variant_list_all_of_instance = FamilyVariantListAllOf.from_json(json)
# print the JSON string representation of the object
print FamilyVariantListAllOf.to_json()

# convert the object into a dict
family_variant_list_all_of_dict = family_variant_list_all_of_instance.to_dict()
# create an instance of FamilyVariantListAllOf from a dict
family_variant_list_all_of_form_dict = family_variant_list_all_of.from_dict(family_variant_list_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


