# MediaFileItemListLinks


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**MediaFileItemListLinksSelf**](MediaFileItemListLinksSelf.md) |  | [optional] 
**download** | [**GetMediaFilesCode200ResponseLinksDownload**](GetMediaFilesCode200ResponseLinksDownload.md) |  | [optional] 

## Example

```python
from akeneo.models.media_file_item_list_links import MediaFileItemListLinks

# TODO update the JSON string below
json = "{}"
# create an instance of MediaFileItemListLinks from a JSON string
media_file_item_list_links_instance = MediaFileItemListLinks.from_json(json)
# print the JSON string representation of the object
print MediaFileItemListLinks.to_json()

# convert the object into a dict
media_file_item_list_links_dict = media_file_item_list_links_instance.to_dict()
# create an instance of MediaFileItemListLinks from a dict
media_file_item_list_links_form_dict = media_file_item_list_links.from_dict(media_file_item_list_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


