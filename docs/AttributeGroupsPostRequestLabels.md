# AttributeGroupsPostRequestLabels

Attribute group labels for each locale

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale_code** | **str** | Attribute group label for the locale &#x60;localeCode&#x60; | [optional] 

## Example

```python
from openapi_client.models.attribute_groups_post_request_labels import AttributeGroupsPostRequestLabels

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeGroupsPostRequestLabels from a JSON string
attribute_groups_post_request_labels_instance = AttributeGroupsPostRequestLabels.from_json(json)
# print the JSON string representation of the object
print AttributeGroupsPostRequestLabels.to_json()

# convert the object into a dict
attribute_groups_post_request_labels_dict = attribute_groups_post_request_labels_instance.to_dict()
# create an instance of AttributeGroupsPostRequestLabels from a dict
attribute_groups_post_request_labels_form_dict = attribute_groups_post_request_labels.from_dict(attribute_groups_post_request_labels_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


