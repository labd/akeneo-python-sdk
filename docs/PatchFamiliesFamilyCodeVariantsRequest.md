# PatchFamiliesFamilyCodeVariantsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Family variant code | 
**variant_attribute_sets** | [**List[FamilyVariantsEmbeddedItemsInnerAllOfVariantAttributeSetsInner]**](FamilyVariantsEmbeddedItemsInnerAllOfVariantAttributeSetsInner.md) | Attributes distribution according to the enrichment level | 
**labels** | [**FamilyVariantsEmbeddedItemsInnerAllOfLabels**](FamilyVariantsEmbeddedItemsInnerAllOfLabels.md) |  | [optional] 

## Example

```python
from akeneo.models.patch_families_family_code_variants_request import PatchFamiliesFamilyCodeVariantsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchFamiliesFamilyCodeVariantsRequest from a JSON string
patch_families_family_code_variants_request_instance = PatchFamiliesFamilyCodeVariantsRequest.from_json(json)
# print the JSON string representation of the object
print PatchFamiliesFamilyCodeVariantsRequest.to_json()

# convert the object into a dict
patch_families_family_code_variants_request_dict = patch_families_family_code_variants_request_instance.to_dict()
# create an instance of PatchFamiliesFamilyCodeVariantsRequest from a dict
patch_families_family_code_variants_request_form_dict = patch_families_family_code_variants_request.from_dict(patch_families_family_code_variants_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


