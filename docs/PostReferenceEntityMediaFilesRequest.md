# PostReferenceEntityMediaFilesRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **str** | The binary of the media file | 

## Example

```python
from akeneo.models.post_reference_entity_media_files_request import PostReferenceEntityMediaFilesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostReferenceEntityMediaFilesRequest from a JSON string
post_reference_entity_media_files_request_instance = PostReferenceEntityMediaFilesRequest.from_json(json)
# print the JSON string representation of the object
print PostReferenceEntityMediaFilesRequest.to_json()

# convert the object into a dict
post_reference_entity_media_files_request_dict = post_reference_entity_media_files_request_instance.to_dict()
# create an instance of PostReferenceEntityMediaFilesRequest from a dict
post_reference_entity_media_files_request_form_dict = post_reference_entity_media_files_request.from_dict(post_reference_entity_media_files_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


