# PostFamiliesFamilyCodeVariantsRequestVariantAttributeSetsInner

Enrichment level

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **int** | Enrichment level | 
**axes** | **List[str]** | Codes of attributes used as variant axes | 
**attributes** | **List[str]** | Codes of attributes bind to this enrichment level | [optional] 

## Example

```python
from openapi_client.models.post_families_family_code_variants_request_variant_attribute_sets_inner import PostFamiliesFamilyCodeVariantsRequestVariantAttributeSetsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostFamiliesFamilyCodeVariantsRequestVariantAttributeSetsInner from a JSON string
post_families_family_code_variants_request_variant_attribute_sets_inner_instance = PostFamiliesFamilyCodeVariantsRequestVariantAttributeSetsInner.from_json(json)
# print the JSON string representation of the object
print PostFamiliesFamilyCodeVariantsRequestVariantAttributeSetsInner.to_json()

# convert the object into a dict
post_families_family_code_variants_request_variant_attribute_sets_inner_dict = post_families_family_code_variants_request_variant_attribute_sets_inner_instance.to_dict()
# create an instance of PostFamiliesFamilyCodeVariantsRequestVariantAttributeSetsInner from a dict
post_families_family_code_variants_request_variant_attribute_sets_inner_form_dict = post_families_family_code_variants_request_variant_attribute_sets_inner.from_dict(post_families_family_code_variants_request_variant_attribute_sets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


