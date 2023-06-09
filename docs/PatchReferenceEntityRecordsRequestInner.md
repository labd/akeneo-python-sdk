# PatchReferenceEntityRecordsRequestInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code of the record | 
**values** | **Dict[str, List[ReferenceEntityRecordEmbeddedItemsInnerAllOfValuesValueInner]]** | Record attributes values, see &lt;a href&#x3D;&#39;/concepts/reference-entities.html#focus-on-the-reference-entity-record-values&#39;&gt;Reference entity record values&lt;/a&gt; section for more details | [optional] 
**created** | **str** | Date of creation. | [optional] [default to 'null']
**updated** | **str** | Date of the last update. | [optional] [default to 'null']

## Example

```python
from akeneo.models.patch_reference_entity_records_request_inner import PatchReferenceEntityRecordsRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of PatchReferenceEntityRecordsRequestInner from a JSON string
patch_reference_entity_records_request_inner_instance = PatchReferenceEntityRecordsRequestInner.from_json(json)
# print the JSON string representation of the object
print PatchReferenceEntityRecordsRequestInner.to_json()

# convert the object into a dict
patch_reference_entity_records_request_inner_dict = patch_reference_entity_records_request_inner_instance.to_dict()
# create an instance of PatchReferenceEntityRecordsRequestInner from a dict
patch_reference_entity_records_request_inner_form_dict = patch_reference_entity_records_request_inner.from_dict(patch_reference_entity_records_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


