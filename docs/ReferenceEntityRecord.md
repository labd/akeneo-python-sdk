# ReferenceEntityRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**ReferenceEntityRecordEmbedded**](ReferenceEntityRecordEmbedded.md) |  | [optional] 
**links** | [**ReferenceEntitiesLinks**](ReferenceEntitiesLinks.md) |  | [optional] 

## Example

```python
from akeneo.models.reference_entity_record import ReferenceEntityRecord

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceEntityRecord from a JSON string
reference_entity_record_instance = ReferenceEntityRecord.from_json(json)
# print the JSON string representation of the object
print ReferenceEntityRecord.to_json()

# convert the object into a dict
reference_entity_record_dict = reference_entity_record_instance.to_dict()
# create an instance of ReferenceEntityRecord from a dict
reference_entity_record_form_dict = reference_entity_record.from_dict(reference_entity_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


