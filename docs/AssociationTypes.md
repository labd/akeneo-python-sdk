# AssociationTypes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**AssociationTypesEmbedded**](AssociationTypesEmbedded.md) |  | [optional] 
**links** | [**ProductsLinks**](ProductsLinks.md) |  | [optional] 
**current_page** | **int** | Current page number | [optional] 

## Example

```python
from akeneo.models.association_types import AssociationTypes

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationTypes from a JSON string
association_types_instance = AssociationTypes.from_json(json)
# print the JSON string representation of the object
print AssociationTypes.to_json()

# convert the object into a dict
association_types_dict = association_types_instance.to_dict()
# create an instance of AssociationTypes from a dict
association_types_form_dict = association_types.from_dict(association_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


