# FamilyVariants


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**FamilyVariantsEmbedded**](FamilyVariantsEmbedded.md) |  | [optional] 
**links** | [**ProductsLinks**](ProductsLinks.md) |  | [optional] 
**current_page** | **int** | Current page number | [optional] 

## Example

```python
from akeneo.models.family_variants import FamilyVariants

# TODO update the JSON string below
json = "{}"
# create an instance of FamilyVariants from a JSON string
family_variants_instance = FamilyVariants.from_json(json)
# print the JSON string representation of the object
print FamilyVariants.to_json()

# convert the object into a dict
family_variants_dict = family_variants_instance.to_dict()
# create an instance of FamilyVariants from a dict
family_variants_form_dict = family_variants.from_dict(family_variants_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


