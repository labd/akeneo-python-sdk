# PostFamiliesFamilyCodeVariantsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Family variant code | 
**variant_attribute_sets** | [**List[PostFamiliesFamilyCodeVariantsRequestVariantAttributeSetsInner]**](PostFamiliesFamilyCodeVariantsRequestVariantAttributeSetsInner.md) | Attributes distribution according to the enrichment level | 
**labels** | [**PostFamiliesFamilyCodeVariantsRequestLabels**](PostFamiliesFamilyCodeVariantsRequestLabels.md) |  | [optional] 

## Example

```python
from akeneo.models.post_families_family_code_variants_request import PostFamiliesFamilyCodeVariantsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostFamiliesFamilyCodeVariantsRequest from a JSON string
post_families_family_code_variants_request_instance = PostFamiliesFamilyCodeVariantsRequest.from_json(json)
# print the JSON string representation of the object
print PostFamiliesFamilyCodeVariantsRequest.to_json()

# convert the object into a dict
post_families_family_code_variants_request_dict = post_families_family_code_variants_request_instance.to_dict()
# create an instance of PostFamiliesFamilyCodeVariantsRequest from a dict
post_families_family_code_variants_request_form_dict = post_families_family_code_variants_request.from_dict(post_families_family_code_variants_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


