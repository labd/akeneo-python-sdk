# PatchReferenceEntityRecords200ResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Resource code | [optional] 
**status_code** | **int** | HTTP status code, see &lt;a href&#x3D;\&quot;/documentation/responses.html#client-errors\&quot;&gt;Client errors&lt;/a&gt; to understand the meaning of each code | [optional] 
**message** | **str** | Message explaining the error | [optional] 

## Example

```python
from openapi_client.models.patch_reference_entity_records200_response_inner import PatchReferenceEntityRecords200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of PatchReferenceEntityRecords200ResponseInner from a JSON string
patch_reference_entity_records200_response_inner_instance = PatchReferenceEntityRecords200ResponseInner.from_json(json)
# print the JSON string representation of the object
print PatchReferenceEntityRecords200ResponseInner.to_json()

# convert the object into a dict
patch_reference_entity_records200_response_inner_dict = patch_reference_entity_records200_response_inner_instance.to_dict()
# create an instance of PatchReferenceEntityRecords200ResponseInner from a dict
patch_reference_entity_records200_response_inner_form_dict = patch_reference_entity_records200_response_inner.from_dict(patch_reference_entity_records200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


