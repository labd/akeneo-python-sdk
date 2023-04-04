# GetAssetFamilyCode200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Asset family code | 
**labels** | [**GetAssetFamilyCode200ResponseLabels**](GetAssetFamilyCode200ResponseLabels.md) |  | [optional] 
**attribute_as_main_media** | **str** | Attribute code that is used as the main media of the asset family. | [optional] [default to 'First media file or media link attribute that was created']
**naming_convention** | [**GetAssetFamilyCode200ResponseNamingConvention**](GetAssetFamilyCode200ResponseNamingConvention.md) |  | [optional] 
**product_link_rules** | [**List[GetAssetFamilyCode200ResponseProductLinkRulesInner]**](GetAssetFamilyCode200ResponseProductLinkRulesInner.md) | The rules that will be run after the asset creation, in order to automatically link the assets of this family to a set of products. To understand the format of this property, see &lt;a href&#x3D;&#39;/concepts/asset-manager.html#focus-on-the-product-link-rule&#39;&gt;here&lt;/a&gt;. | [optional] 
**transformations** | [**List[GetAssetFamilyCode200ResponseTransformationsInner]**](GetAssetFamilyCode200ResponseTransformationsInner.md) | The transformations to perform on source files in order to generate new files into your asset attributes (only available since v4.0). To understand the format of this property, see &lt;a href&#x3D;&#39;/concepts/asset-manager.html#focus-on-the-transformations&#39;&gt;here&lt;/a&gt;. | [optional] 

## Example

```python
from akeneo.models.get_asset_family_code200_response import GetAssetFamilyCode200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetFamilyCode200Response from a JSON string
get_asset_family_code200_response_instance = GetAssetFamilyCode200Response.from_json(json)
# print the JSON string representation of the object
print GetAssetFamilyCode200Response.to_json()

# convert the object into a dict
get_asset_family_code200_response_dict = get_asset_family_code200_response_instance.to_dict()
# create an instance of GetAssetFamilyCode200Response from a dict
get_asset_family_code200_response_form_dict = get_asset_family_code200_response.from_dict(get_asset_family_code200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


