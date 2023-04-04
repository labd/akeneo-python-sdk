# PostCategoriesRequestLabels

Category labels for each locale

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale_code** | **str** | Category label for the locale &#x60;localeCode&#x60; | [optional] 

## Example

```python
from akeneo.models.post_categories_request_labels import PostCategoriesRequestLabels

# TODO update the JSON string below
json = "{}"
# create an instance of PostCategoriesRequestLabels from a JSON string
post_categories_request_labels_instance = PostCategoriesRequestLabels.from_json(json)
# print the JSON string representation of the object
print PostCategoriesRequestLabels.to_json()

# convert the object into a dict
post_categories_request_labels_dict = post_categories_request_labels_instance.to_dict()
# create an instance of PostCategoriesRequestLabels from a dict
post_categories_request_labels_form_dict = post_categories_request_labels.from_dict(post_categories_request_labels_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


