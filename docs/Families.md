# Families


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**FamiliesEmbedded**](FamiliesEmbedded.md) |  | [optional] 
**links** | [**ProductsLinks**](ProductsLinks.md) |  | [optional] 
**current_page** | **int** | Current page number | [optional] 

## Example

```python
from akeneo.models.families import Families

# TODO update the JSON string below
json = "{}"
# create an instance of Families from a JSON string
families_instance = Families.from_json(json)
# print the JSON string representation of the object
print Families.to_json()

# convert the object into a dict
families_dict = families_instance.to_dict()
# create an instance of Families from a dict
families_form_dict = families.from_dict(families_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


