# PAMAssetCategoriesEmbeddedItemsInnerAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | PAM asset category code | 
**parent** | **str** | PAM ssset category code of the parent&#39;s asset category | [optional] [default to 'null']
**labels** | [**PAMAssetCategoriesEmbeddedItemsInnerAllOfLabels**](PAMAssetCategoriesEmbeddedItemsInnerAllOfLabels.md) |  | [optional] 

## Example

```python
from akeneo.models.pam_asset_categories_embedded_items_inner_all_of import PAMAssetCategoriesEmbeddedItemsInnerAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of PAMAssetCategoriesEmbeddedItemsInnerAllOf from a JSON string
pam_asset_categories_embedded_items_inner_all_of_instance = PAMAssetCategoriesEmbeddedItemsInnerAllOf.from_json(json)
# print the JSON string representation of the object
print PAMAssetCategoriesEmbeddedItemsInnerAllOf.to_json()

# convert the object into a dict
pam_asset_categories_embedded_items_inner_all_of_dict = pam_asset_categories_embedded_items_inner_all_of_instance.to_dict()
# create an instance of PAMAssetCategoriesEmbeddedItemsInnerAllOf from a dict
pam_asset_categories_embedded_items_inner_all_of_form_dict = pam_asset_categories_embedded_items_inner_all_of.from_dict(pam_asset_categories_embedded_items_inner_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


