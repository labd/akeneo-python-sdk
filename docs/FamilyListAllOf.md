# FamilyListAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Family code | 
**attribute_as_label** | **str** | Attribute code used as label | 
**attribute_as_image** | **str** | Attribute code used as the main picture in the user interface (only since v2.0) | [optional] [default to 'null']
**attributes** | **List[str]** | Attributes codes that compose the family | [optional] 
**attribute_requirements** | [**FamilyListAllOfAttributeRequirements**](FamilyListAllOfAttributeRequirements.md) |  | [optional] 
**labels** | [**FamilyListAllOfLabels**](FamilyListAllOfLabels.md) |  | [optional] 

## Example

```python
from openapi_client.models.family_list_all_of import FamilyListAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of FamilyListAllOf from a JSON string
family_list_all_of_instance = FamilyListAllOf.from_json(json)
# print the JSON string representation of the object
print FamilyListAllOf.to_json()

# convert the object into a dict
family_list_all_of_dict = family_list_all_of_instance.to_dict()
# create an instance of FamilyListAllOf from a dict
family_list_all_of_form_dict = family_list_all_of.from_dict(family_list_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


