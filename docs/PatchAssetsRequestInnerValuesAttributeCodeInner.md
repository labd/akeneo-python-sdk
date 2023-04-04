# PatchAssetsRequestInnerValuesAttributeCodeInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** | Channel code of the asset attribute value | [optional] 
**locale** | **str** | Locale code of the asset attribute value | [optional] 
**data** | **object** | Asset attribute value. See &lt;a href&#x3D;&#39;/concepts/asset-manager.html#the-data-format&#39;&gt;the &#x60;data&#x60; format&lt;/a&gt; section for more details. | [optional] 

## Example

```python
from akeneo.models.patch_assets_request_inner_values_attribute_code_inner import PatchAssetsRequestInnerValuesAttributeCodeInner

# TODO update the JSON string below
json = "{}"
# create an instance of PatchAssetsRequestInnerValuesAttributeCodeInner from a JSON string
patch_assets_request_inner_values_attribute_code_inner_instance = PatchAssetsRequestInnerValuesAttributeCodeInner.from_json(json)
# print the JSON string representation of the object
print PatchAssetsRequestInnerValuesAttributeCodeInner.to_json()

# convert the object into a dict
patch_assets_request_inner_values_attribute_code_inner_dict = patch_assets_request_inner_values_attribute_code_inner_instance.to_dict()
# create an instance of PatchAssetsRequestInnerValuesAttributeCodeInner from a dict
patch_assets_request_inner_values_attribute_code_inner_form_dict = patch_assets_request_inner_values_attribute_code_inner.from_dict(patch_assets_request_inner_values_attribute_code_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


