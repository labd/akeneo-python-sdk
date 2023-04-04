# DeprecatedAssetCategoryList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ProductListAllOfLinks**](ProductListAllOfLinks.md) |  | [optional] 
**code** | **str** | PAM asset category code | 
**parent** | **str** | PAM ssset category code of the parent&#39;s asset category | [optional] [default to 'null']
**labels** | [**DeprecatedAssetCategoryListAllOfLabels**](DeprecatedAssetCategoryListAllOfLabels.md) |  | [optional] 

## Example

```python
from akeneo.models.deprecated_asset_category_list import DeprecatedAssetCategoryList

# TODO update the JSON string below
json = "{}"
# create an instance of DeprecatedAssetCategoryList from a JSON string
deprecated_asset_category_list_instance = DeprecatedAssetCategoryList.from_json(json)
# print the JSON string representation of the object
print DeprecatedAssetCategoryList.to_json()

# convert the object into a dict
deprecated_asset_category_list_dict = deprecated_asset_category_list_instance.to_dict()
# create an instance of DeprecatedAssetCategoryList from a dict
deprecated_asset_category_list_form_dict = deprecated_asset_category_list.from_dict(deprecated_asset_category_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


