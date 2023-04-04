# ReferenceEntityItemListLinks


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**AssetFamilyItemListLinksSelf**](AssetFamilyItemListLinksSelf.md) |  | [optional] 
**image_download** | [**GetReferenceEntitiesCode200ResponseLinksImageDownload**](GetReferenceEntitiesCode200ResponseLinksImageDownload.md) |  | [optional] 

## Example

```python
from openapi_client.models.reference_entity_item_list_links import ReferenceEntityItemListLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceEntityItemListLinks from a JSON string
reference_entity_item_list_links_instance = ReferenceEntityItemListLinks.from_json(json)
# print the JSON string representation of the object
print ReferenceEntityItemListLinks.to_json()

# convert the object into a dict
reference_entity_item_list_links_dict = reference_entity_item_list_links_instance.to_dict()
# create an instance of ReferenceEntityItemListLinks from a dict
reference_entity_item_list_links_form_dict = reference_entity_item_list_links.from_dict(reference_entity_item_list_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


