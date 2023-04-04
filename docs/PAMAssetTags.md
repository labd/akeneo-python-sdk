# PAMAssetTags


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**PAMAssetTagsEmbedded**](PAMAssetTagsEmbedded.md) |  | [optional] 
**links** | [**ProductsLinks**](ProductsLinks.md) |  | [optional] 
**current_page** | **int** | Current page number | [optional] 

## Example

```python
from akeneo.models.pam_asset_tags import PAMAssetTags

# TODO update the JSON string below
json = "{}"
# create an instance of PAMAssetTags from a JSON string
pam_asset_tags_instance = PAMAssetTags.from_json(json)
# print the JSON string representation of the object
print PAMAssetTags.to_json()

# convert the object into a dict
pam_asset_tags_dict = pam_asset_tags_instance.to_dict()
# create an instance of PAMAssetTags from a dict
pam_asset_tags_form_dict = pam_asset_tags.from_dict(pam_asset_tags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


