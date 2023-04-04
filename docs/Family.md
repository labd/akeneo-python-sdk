# Family


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Family code | 
**attribute_as_label** | **str** | Attribute code used as label | 
**attribute_as_image** | **str** | Attribute code used as the main picture in the user interface (only since v2.0) | [optional] [default to 'null']
**attributes** | **List[str]** | Attributes codes that compose the family | [optional] 
**attribute_requirements** | [**FamiliesEmbeddedItemsInnerAllOfAttributeRequirements**](FamiliesEmbeddedItemsInnerAllOfAttributeRequirements.md) |  | [optional] 
**labels** | [**FamiliesEmbeddedItemsInnerAllOfLabels**](FamiliesEmbeddedItemsInnerAllOfLabels.md) |  | [optional] 

## Example

```python
from akeneo.models.family import Family

# TODO update the JSON string below
json = "{}"
# create an instance of Family from a JSON string
family_instance = Family.from_json(json)
# print the JSON string representation of the object
print Family.to_json()

# convert the object into a dict
family_dict = family_instance.to_dict()
# create an instance of Family from a dict
family_form_dict = family.from_dict(family_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


