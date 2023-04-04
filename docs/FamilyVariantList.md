# FamilyVariantList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ProductListAllOfLinks**](ProductListAllOfLinks.md) |  | [optional] 
**code** | **str** | Family variant code | 
**variant_attribute_sets** | [**List[FamilyVariantListAllOfVariantAttributeSets]**](FamilyVariantListAllOfVariantAttributeSets.md) | Attributes distribution according to the enrichment level | 
**labels** | [**FamilyVariantListAllOfLabels**](FamilyVariantListAllOfLabels.md) |  | [optional] 

## Example

```python
from openapi_client.models.family_variant_list import FamilyVariantList

# TODO update the JSON string below
json = "{}"
# create an instance of FamilyVariantList from a JSON string
family_variant_list_instance = FamilyVariantList.from_json(json)
# print the JSON string representation of the object
print FamilyVariantList.to_json()

# convert the object into a dict
family_variant_list_dict = family_variant_list_instance.to_dict()
# create an instance of FamilyVariantList from a dict
family_variant_list_form_dict = family_variant_list.from_dict(family_variant_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


