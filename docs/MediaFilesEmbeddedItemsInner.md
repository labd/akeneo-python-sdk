# MediaFilesEmbeddedItemsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**MediaFilesEmbeddedItemsInnerAllOfLinks**](MediaFilesEmbeddedItemsInnerAllOfLinks.md) |  | [optional] 
**code** | **str** | Media file code | [optional] 
**original_filename** | **str** | Original filename of the media file | [optional] 
**mime_type** | **str** | Mime type of the media file | [optional] 
**size** | **int** | Size of the media file | [optional] 
**extension** | **str** | Extension of the media file | [optional] 

## Example

```python
from akeneo.models.media_files_embedded_items_inner import MediaFilesEmbeddedItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MediaFilesEmbeddedItemsInner from a JSON string
media_files_embedded_items_inner_instance = MediaFilesEmbeddedItemsInner.from_json(json)
# print the JSON string representation of the object
print MediaFilesEmbeddedItemsInner.to_json()

# convert the object into a dict
media_files_embedded_items_inner_dict = media_files_embedded_items_inner_instance.to_dict()
# create an instance of MediaFilesEmbeddedItemsInner from a dict
media_files_embedded_items_inner_form_dict = media_files_embedded_items_inner.from_dict(media_files_embedded_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


