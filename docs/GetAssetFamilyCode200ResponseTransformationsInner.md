# GetAssetFamilyCode200ResponseTransformationsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The name of the transformation | 
**filename_suffix** | **str** | The suffix that will be appended to the source filename to generate the target filename. More details &lt;a href&#x3D;&#39;/concepts/asset-manager.html#target-filename&#39;&gt;here&lt;/a&gt;. | [optional] 
**filename_prefix** | **str** | The prefix that will be prepended to the source filename to generate the target filename. More details &lt;a href&#x3D;&#39;/concepts/asset-manager.html#target-filename&#39;&gt;here&lt;/a&gt;. | [optional] 
**source** | [**GetAssetFamilyCode200ResponseTransformationsInnerSource**](GetAssetFamilyCode200ResponseTransformationsInnerSource.md) |  | 
**target** | [**GetAssetFamilyCode200ResponseTransformationsInnerTarget**](GetAssetFamilyCode200ResponseTransformationsInnerTarget.md) |  | 
**operations** | [**GetAssetFamilyCode200ResponseTransformationsInnerOperations**](GetAssetFamilyCode200ResponseTransformationsInnerOperations.md) |  | 

## Example

```python
from openapi_client.models.get_asset_family_code200_response_transformations_inner import GetAssetFamilyCode200ResponseTransformationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetFamilyCode200ResponseTransformationsInner from a JSON string
get_asset_family_code200_response_transformations_inner_instance = GetAssetFamilyCode200ResponseTransformationsInner.from_json(json)
# print the JSON string representation of the object
print GetAssetFamilyCode200ResponseTransformationsInner.to_json()

# convert the object into a dict
get_asset_family_code200_response_transformations_inner_dict = get_asset_family_code200_response_transformations_inner_instance.to_dict()
# create an instance of GetAssetFamilyCode200ResponseTransformationsInner from a dict
get_asset_family_code200_response_transformations_inner_form_dict = get_asset_family_code200_response_transformations_inner.from_dict(get_asset_family_code200_response_transformations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


