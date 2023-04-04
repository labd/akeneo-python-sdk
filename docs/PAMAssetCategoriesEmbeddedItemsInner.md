# PAMAssetCategoriesEmbeddedItemsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ProductsEmbeddedItemsInnerAllOfLinks**](ProductsEmbeddedItemsInnerAllOfLinks.md) |  | [optional] 
**code** | **str** | PAM asset category code | 
**parent** | **str** | PAM ssset category code of the parent&#39;s asset category | [optional] [default to 'null']
**labels** | [**PAMAssetCategoriesEmbeddedItemsInnerAllOfLabels**](PAMAssetCategoriesEmbeddedItemsInnerAllOfLabels.md) |  | [optional] 

## Example

```python
from akeneo.models.pam_asset_categories_embedded_items_inner import PAMAssetCategoriesEmbeddedItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PAMAssetCategoriesEmbeddedItemsInner from a JSON string
pam_asset_categories_embedded_items_inner_instance = PAMAssetCategoriesEmbeddedItemsInner.from_json(json)
# print the JSON string representation of the object
print PAMAssetCategoriesEmbeddedItemsInner.to_json()

# convert the object into a dict
pam_asset_categories_embedded_items_inner_dict = pam_asset_categories_embedded_items_inner_instance.to_dict()
# create an instance of PAMAssetCategoriesEmbeddedItemsInner from a dict
pam_asset_categories_embedded_items_inner_form_dict = pam_asset_categories_embedded_items_inner.from_dict(pam_asset_categories_embedded_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


