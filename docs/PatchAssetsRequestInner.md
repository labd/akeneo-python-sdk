# PatchAssetsRequestInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code of the asset | 
**values** | **Dict[str, List[AssetEmbeddedItemsInnerAllOfValuesValueInner]]** | Asset attributes values, see the &lt;a href&#x3D;&#39;/concepts/asset-manager.html#focus-on-the-asset-values&#39;&gt;Focus on the asset values&lt;/a&gt; section for more details. | [optional] 
**created** | **str** | Date of creation | [optional] 
**updated** | **str** | Date of the last update | [optional] 

## Example

```python
from openapi_client.models.patch_assets_request_inner import PatchAssetsRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of PatchAssetsRequestInner from a JSON string
patch_assets_request_inner_instance = PatchAssetsRequestInner.from_json(json)
# print the JSON string representation of the object
print PatchAssetsRequestInner.to_json()

# convert the object into a dict
patch_assets_request_inner_dict = patch_assets_request_inner_instance.to_dict()
# create an instance of PatchAssetsRequestInner from a dict
patch_assets_request_inner_form_dict = patch_assets_request_inner.from_dict(patch_assets_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


