# PatchReferenceEntityRecordsRequestInnerValues

Record attributes values, see <a href='/concepts/reference-entities.html#focus-on-the-reference-entity-record-values'>Reference entity record values</a> section for more details

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_code** | [**List[PatchReferenceEntityRecordsRequestInnerValuesAttributeCodeInner]**](PatchReferenceEntityRecordsRequestInnerValuesAttributeCodeInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.patch_reference_entity_records_request_inner_values import PatchReferenceEntityRecordsRequestInnerValues

# TODO update the JSON string below
json = "{}"
# create an instance of PatchReferenceEntityRecordsRequestInnerValues from a JSON string
patch_reference_entity_records_request_inner_values_instance = PatchReferenceEntityRecordsRequestInnerValues.from_json(json)
# print the JSON string representation of the object
print PatchReferenceEntityRecordsRequestInnerValues.to_json()

# convert the object into a dict
patch_reference_entity_records_request_inner_values_dict = patch_reference_entity_records_request_inner_values_instance.to_dict()
# create an instance of PatchReferenceEntityRecordsRequestInnerValues from a dict
patch_reference_entity_records_request_inner_values_form_dict = patch_reference_entity_records_request_inner_values.from_dict(patch_reference_entity_records_request_inner_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


