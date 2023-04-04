# DeprecatedAssetCategory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | PAM asset category code | 
**parent** | **str** | PAM ssset category code of the parent&#39;s asset category | [optional] [default to 'null']
**labels** | [**PAMAssetCategoriesEmbeddedItemsInnerAllOfLabels**](PAMAssetCategoriesEmbeddedItemsInnerAllOfLabels.md) |  | [optional] 

## Example

```python
from akeneo.models.deprecated_asset_category import DeprecatedAssetCategory

# TODO update the JSON string below
json = "{}"
# create an instance of DeprecatedAssetCategory from a JSON string
deprecated_asset_category_instance = DeprecatedAssetCategory.from_json(json)
# print the JSON string representation of the object
print DeprecatedAssetCategory.to_json()

# convert the object into a dict
deprecated_asset_category_dict = deprecated_asset_category_instance.to_dict()
# create an instance of DeprecatedAssetCategory from a dict
deprecated_asset_category_form_dict = deprecated_asset_category.from_dict(deprecated_asset_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


