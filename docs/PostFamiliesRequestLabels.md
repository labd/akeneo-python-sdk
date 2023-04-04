# PostFamiliesRequestLabels

Family labels for each locale

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale_code** | **str** | Family label for the locale &#x60;localeCode&#x60; | [optional] 

## Example

```python
from openapi_client.models.post_families_request_labels import PostFamiliesRequestLabels

# TODO update the JSON string below
json = "{}"
# create an instance of PostFamiliesRequestLabels from a JSON string
post_families_request_labels_instance = PostFamiliesRequestLabels.from_json(json)
# print the JSON string representation of the object
print PostFamiliesRequestLabels.to_json()

# convert the object into a dict
post_families_request_labels_dict = post_families_request_labels_instance.to_dict()
# create an instance of PostFamiliesRequestLabels from a dict
post_families_request_labels_form_dict = post_families_request_labels.from_dict(post_families_request_labels_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


