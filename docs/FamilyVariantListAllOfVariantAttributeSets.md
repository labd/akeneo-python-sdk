# FamilyVariantListAllOfVariantAttributeSets

Enrichment level

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **int** | Enrichment level | 
**axes** | **List[str]** | Codes of attributes used as variant axes | 
**attributes** | **List[str]** | Codes of attributes bind to this enrichment level | [optional] 

## Example

```python
from akeneo.models.family_variant_list_all_of_variant_attribute_sets import FamilyVariantListAllOfVariantAttributeSets

# TODO update the JSON string below
json = "{}"
# create an instance of FamilyVariantListAllOfVariantAttributeSets from a JSON string
family_variant_list_all_of_variant_attribute_sets_instance = FamilyVariantListAllOfVariantAttributeSets.from_json(json)
# print the JSON string representation of the object
print FamilyVariantListAllOfVariantAttributeSets.to_json()

# convert the object into a dict
family_variant_list_all_of_variant_attribute_sets_dict = family_variant_list_all_of_variant_attribute_sets_instance.to_dict()
# create an instance of FamilyVariantListAllOfVariantAttributeSets from a dict
family_variant_list_all_of_variant_attribute_sets_form_dict = family_variant_list_all_of_variant_attribute_sets.from_dict(family_variant_list_all_of_variant_attribute_sets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


