# PAMAssetCategories


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**PAMAssetCategoriesEmbedded**](PAMAssetCategoriesEmbedded.md) |  | [optional] 
**links** | [**ProductsLinks**](ProductsLinks.md) |  | [optional] 
**current_page** | **int** | Current page number | [optional] 

## Example

```python
from akeneo.models.pam_asset_categories import PAMAssetCategories

# TODO update the JSON string below
json = "{}"
# create an instance of PAMAssetCategories from a JSON string
pam_asset_categories_instance = PAMAssetCategories.from_json(json)
# print the JSON string representation of the object
print PAMAssetCategories.to_json()

# convert the object into a dict
pam_asset_categories_dict = pam_asset_categories_instance.to_dict()
# create an instance of PAMAssetCategories from a dict
pam_asset_categories_form_dict = pam_asset_categories.from_dict(pam_asset_categories_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


