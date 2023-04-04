# PostCategoriesRequestValues

Attribute values

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_code_attribute_uuid_channel_code_locale_code** | [**List[PostCategoriesRequestValuesAttributeCodeAttributeUuidChannelCodeLocaleCodeInner]**](PostCategoriesRequestValuesAttributeCodeAttributeUuidChannelCodeLocaleCodeInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.post_categories_request_values import PostCategoriesRequestValues

# TODO update the JSON string below
json = "{}"
# create an instance of PostCategoriesRequestValues from a JSON string
post_categories_request_values_instance = PostCategoriesRequestValues.from_json(json)
# print the JSON string representation of the object
print PostCategoriesRequestValues.to_json()

# convert the object into a dict
post_categories_request_values_dict = post_categories_request_values_instance.to_dict()
# create an instance of PostCategoriesRequestValues from a dict
post_categories_request_values_form_dict = post_categories_request_values.from_dict(post_categories_request_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


