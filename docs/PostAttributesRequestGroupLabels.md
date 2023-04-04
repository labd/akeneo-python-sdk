# PostAttributesRequestGroupLabels

Group labels for each locale

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale_code** | **str** | Group label for the locale &#x60;localeCode&#x60; | [optional] 

## Example

```python
from openapi_client.models.post_attributes_request_group_labels import PostAttributesRequestGroupLabels

# TODO update the JSON string below
json = "{}"
# create an instance of PostAttributesRequestGroupLabels from a JSON string
post_attributes_request_group_labels_instance = PostAttributesRequestGroupLabels.from_json(json)
# print the JSON string representation of the object
print PostAttributesRequestGroupLabels.to_json()

# convert the object into a dict
post_attributes_request_group_labels_dict = post_attributes_request_group_labels_instance.to_dict()
# create an instance of PostAttributesRequestGroupLabels from a dict
post_attributes_request_group_labels_form_dict = post_attributes_request_group_labels.from_dict(post_attributes_request_group_labels_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


