# DeprecatedAssetCategoryListAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | PAM asset category code | 
**parent** | **str** | PAM ssset category code of the parent&#39;s asset category | [optional] [default to 'null']
**labels** | [**DeprecatedAssetCategoryListAllOfLabels**](DeprecatedAssetCategoryListAllOfLabels.md) |  | [optional] 

## Example

```python
from akeneo.models.deprecated_asset_category_list_all_of import DeprecatedAssetCategoryListAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of DeprecatedAssetCategoryListAllOf from a JSON string
deprecated_asset_category_list_all_of_instance = DeprecatedAssetCategoryListAllOf.from_json(json)
# print the JSON string representation of the object
print DeprecatedAssetCategoryListAllOf.to_json()

# convert the object into a dict
deprecated_asset_category_list_all_of_dict = deprecated_asset_category_list_all_of_instance.to_dict()
# create an instance of DeprecatedAssetCategoryListAllOf from a dict
deprecated_asset_category_list_all_of_form_dict = deprecated_asset_category_list_all_of.from_dict(deprecated_asset_category_list_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


