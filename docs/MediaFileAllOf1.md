# MediaFileAllOf1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Media file code | [optional] 
**original_filename** | **str** | Original filename of the media file | [optional] 
**mime_type** | **str** | Mime type of the media file | [optional] 
**size** | **int** | Size of the media file | [optional] 
**extension** | **str** | Extension of the media file | [optional] 

## Example

```python
from akeneo.models.media_file_all_of1 import MediaFileAllOf1

# TODO update the JSON string below
json = "{}"
# create an instance of MediaFileAllOf1 from a JSON string
media_file_all_of1_instance = MediaFileAllOf1.from_json(json)
# print the JSON string representation of the object
print MediaFileAllOf1.to_json()

# convert the object into a dict
media_file_all_of1_dict = media_file_all_of1_instance.to_dict()
# create an instance of MediaFileAllOf1 from a dict
media_file_all_of1_form_dict = media_file_all_of1.from_dict(media_file_all_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


