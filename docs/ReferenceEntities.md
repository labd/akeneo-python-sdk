# ReferenceEntities


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**ReferenceEntitiesEmbedded**](ReferenceEntitiesEmbedded.md) |  | [optional] 
**links** | [**ReferenceEntitiesLinks**](ReferenceEntitiesLinks.md) |  | [optional] 

## Example

```python
from akeneo.models.reference_entities import ReferenceEntities

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceEntities from a JSON string
reference_entities_instance = ReferenceEntities.from_json(json)
# print the JSON string representation of the object
print ReferenceEntities.to_json()

# convert the object into a dict
reference_entities_dict = reference_entities_instance.to_dict()
# create an instance of ReferenceEntities from a dict
reference_entities_form_dict = reference_entities.from_dict(reference_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


