# PatchAssetsRequestInnerValues

Asset attributes values, see the <a href='/concepts/asset-manager.html#focus-on-the-asset-values'>Focus on the asset values</a> section for more details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_code** | [**List[PatchAssetsRequestInnerValuesAttributeCodeInner]**](PatchAssetsRequestInnerValuesAttributeCodeInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.patch_assets_request_inner_values import PatchAssetsRequestInnerValues

# TODO update the JSON string below
json = "{}"
# create an instance of PatchAssetsRequestInnerValues from a JSON string
patch_assets_request_inner_values_instance = PatchAssetsRequestInnerValues.from_json(json)
# print the JSON string representation of the object
print PatchAssetsRequestInnerValues.to_json()

# convert the object into a dict
patch_assets_request_inner_values_dict = patch_assets_request_inner_values_instance.to_dict()
# create an instance of PatchAssetsRequestInnerValues from a dict
patch_assets_request_inner_values_form_dict = patch_assets_request_inner_values.from_dict(patch_assets_request_inner_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


