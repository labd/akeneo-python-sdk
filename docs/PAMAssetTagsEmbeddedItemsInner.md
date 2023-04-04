# PAMAssetTagsEmbeddedItemsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ProductsEmbeddedItemsInnerAllOfLinks**](ProductsEmbeddedItemsInnerAllOfLinks.md) |  | [optional] 
**code** | **str** | PAM asset tag code | 

## Example

```python
from akeneo.models.pam_asset_tags_embedded_items_inner import PAMAssetTagsEmbeddedItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PAMAssetTagsEmbeddedItemsInner from a JSON string
pam_asset_tags_embedded_items_inner_instance = PAMAssetTagsEmbeddedItemsInner.from_json(json)
# print the JSON string representation of the object
print PAMAssetTagsEmbeddedItemsInner.to_json()

# convert the object into a dict
pam_asset_tags_embedded_items_inner_dict = pam_asset_tags_embedded_items_inner_instance.to_dict()
# create an instance of PAMAssetTagsEmbeddedItemsInner from a dict
pam_asset_tags_embedded_items_inner_form_dict = pam_asset_tags_embedded_items_inner.from_dict(pam_asset_tags_embedded_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


