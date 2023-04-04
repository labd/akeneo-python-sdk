# GetAssetFamilyCode200ResponseNamingConvention

The naming convention ran over the asset code or the main media filename upon each asset creation, in order to automatically set several values in asset attributes. To learn more and see the format of this property, take a look at <a href='/concepts/asset-manager.html#focus-on-the-naming-convention'>here</a>.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **object** | The string on which the naming convention should be applied. More details &lt;a href&#x3D;&#39;/concepts/asset-manager.html#source&#39;&gt;here&lt;/a&gt;. | [optional] 
**pattern** | **str** | The regular expression that should be applied on the source. More details &lt;a href&#x3D;&#39;/concepts/asset-manager.html#pattern&#39;&gt;here&lt;/a&gt;. | [optional] 
**abort_asset_creation_on_error** | **bool** | Whether the asset should be created if the naming convention failed to apply. More details &lt;a href&#x3D;&#39;/concepts/asset-manager.html#abort-asset-creation-on-error&#39;&gt;here&lt;/a&gt;. | [optional] 

## Example

```python
from openapi_client.models.get_asset_family_code200_response_naming_convention import GetAssetFamilyCode200ResponseNamingConvention

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetFamilyCode200ResponseNamingConvention from a JSON string
get_asset_family_code200_response_naming_convention_instance = GetAssetFamilyCode200ResponseNamingConvention.from_json(json)
# print the JSON string representation of the object
print GetAssetFamilyCode200ResponseNamingConvention.to_json()

# convert the object into a dict
get_asset_family_code200_response_naming_convention_dict = get_asset_family_code200_response_naming_convention_instance.to_dict()
# create an instance of GetAssetFamilyCode200ResponseNamingConvention from a dict
get_asset_family_code200_response_naming_convention_form_dict = get_asset_family_code200_response_naming_convention.from_dict(get_asset_family_code200_response_naming_convention_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


