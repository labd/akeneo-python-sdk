# DeprecatedAssetListAllOfLink

Links to get and download the variation file

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**DeprecatedAssetListAllOfLinkSelf**](DeprecatedAssetListAllOfLinkSelf.md) |  | [optional] 
**download** | [**DeprecatedAssetListAllOfLinkDownload**](DeprecatedAssetListAllOfLinkDownload.md) |  | [optional] 

## Example

```python
from akeneo.models.deprecated_asset_list_all_of_link import DeprecatedAssetListAllOfLink

# TODO update the JSON string below
json = "{}"
# create an instance of DeprecatedAssetListAllOfLink from a JSON string
deprecated_asset_list_all_of_link_instance = DeprecatedAssetListAllOfLink.from_json(json)
# print the JSON string representation of the object
print DeprecatedAssetListAllOfLink.to_json()

# convert the object into a dict
deprecated_asset_list_all_of_link_dict = deprecated_asset_list_all_of_link_instance.to_dict()
# create an instance of DeprecatedAssetListAllOfLink from a dict
deprecated_asset_list_all_of_link_form_dict = deprecated_asset_list_all_of_link.from_dict(deprecated_asset_list_all_of_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


