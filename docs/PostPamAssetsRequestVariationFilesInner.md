# PostPamAssetsRequestVariationFilesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | [**PostPamAssetsRequestVariationFilesInnerLink**](PostPamAssetsRequestVariationFilesInnerLink.md) |  | [optional] 
**locale** | **str** | Locale code of the variation | [optional] 
**scope** | **str** | Channel code of the variation | [optional] 
**code** | **str** | Code of the variation | [optional] 

## Example

```python
from openapi_client.models.post_pam_assets_request_variation_files_inner import PostPamAssetsRequestVariationFilesInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostPamAssetsRequestVariationFilesInner from a JSON string
post_pam_assets_request_variation_files_inner_instance = PostPamAssetsRequestVariationFilesInner.from_json(json)
# print the JSON string representation of the object
print PostPamAssetsRequestVariationFilesInner.to_json()

# convert the object into a dict
post_pam_assets_request_variation_files_inner_dict = post_pam_assets_request_variation_files_inner_instance.to_dict()
# create an instance of PostPamAssetsRequestVariationFilesInner from a dict
post_pam_assets_request_variation_files_inner_form_dict = post_pam_assets_request_variation_files_inner.from_dict(post_pam_assets_request_variation_files_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


