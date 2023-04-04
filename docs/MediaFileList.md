# MediaFileList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**MediaFileListAllOfLinks**](MediaFileListAllOfLinks.md) |  | [optional] 
**code** | **str** | Media file code | [optional] 
**original_filename** | **str** | Original filename of the media file | [optional] 
**mime_type** | **str** | Mime type of the media file | [optional] 
**size** | **int** | Size of the media file | [optional] 
**extension** | **str** | Extension of the media file | [optional] 

## Example

```python
from akeneo.models.media_file_list import MediaFileList

# TODO update the JSON string below
json = "{}"
# create an instance of MediaFileList from a JSON string
media_file_list_instance = MediaFileList.from_json(json)
# print the JSON string representation of the object
print MediaFileList.to_json()

# convert the object into a dict
media_file_list_dict = media_file_list_instance.to_dict()
# create an instance of MediaFileList from a dict
media_file_list_form_dict = media_file_list.from_dict(media_file_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


