# DeprecatedAssetListAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | PAM asset code | 
**categories** | **List[str]** | Codes of the PAM asset categories in which the asset is classified | [optional] 
**description** | **str** | Description of the PAM asset | [optional] [default to 'null']
**localizable** | **bool** | Whether the asset is localized or not, meaning if you want to have different reference files for each of your locale | [optional] [default to False]
**tags** | **List[str]** | Tags of the PAM asset | [optional] 
**end_of_use** | **str** | Date on which the PAM asset expire | [optional] [default to 'null']
**variation_files** | [**List[DeprecatedAssetListAllOfVariationFiles]**](DeprecatedAssetListAllOfVariationFiles.md) | Variations of the PAM asset | [optional] 
**reference_files** | [**List[DeprecatedAssetListAllOfReferenceFiles]**](DeprecatedAssetListAllOfReferenceFiles.md) | Reference files of the PAM asset | [optional] 

## Example

```python
from akeneo.models.deprecated_asset_list_all_of import DeprecatedAssetListAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of DeprecatedAssetListAllOf from a JSON string
deprecated_asset_list_all_of_instance = DeprecatedAssetListAllOf.from_json(json)
# print the JSON string representation of the object
print DeprecatedAssetListAllOf.to_json()

# convert the object into a dict
deprecated_asset_list_all_of_dict = deprecated_asset_list_all_of_instance.to_dict()
# create an instance of DeprecatedAssetListAllOf from a dict
deprecated_asset_list_all_of_form_dict = deprecated_asset_list_all_of.from_dict(deprecated_asset_list_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


