# PostAssetCategoriesRequestLabels

PAM asset category labels for each locale

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale_code** | **str** | PAM asset category label for the locale &#x60;localeCode&#x60; | [optional] 

## Example

```python
from akeneo.models.post_asset_categories_request_labels import PostAssetCategoriesRequestLabels

# TODO update the JSON string below
json = "{}"
# create an instance of PostAssetCategoriesRequestLabels from a JSON string
post_asset_categories_request_labels_instance = PostAssetCategoriesRequestLabels.from_json(json)
# print the JSON string representation of the object
print PostAssetCategoriesRequestLabels.to_json()

# convert the object into a dict
post_asset_categories_request_labels_dict = post_asset_categories_request_labels_instance.to_dict()
# create an instance of PostAssetCategoriesRequestLabels from a dict
post_asset_categories_request_labels_form_dict = post_asset_categories_request_labels.from_dict(post_asset_categories_request_labels_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


