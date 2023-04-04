# PostCategoriesRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Category code | 
**parent** | **str** | Category code of the parent&#39;s category | [optional] [default to 'null']
**updated** | **str** | Date of the last update | [optional] 
**position** | **int** | Position of the category in its level, start from 1 (only available since the 7.0 version and when query parameter \&quot;with_position\&quot; is set to \&quot;true\&quot;) | [optional] 
**labels** | [**PostCategoriesRequestLabels**](PostCategoriesRequestLabels.md) |  | [optional] 
**values** | [**PostCategoriesRequestValues**](PostCategoriesRequestValues.md) |  | [optional] 

## Example

```python
from openapi_client.models.post_categories_request import PostCategoriesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostCategoriesRequest from a JSON string
post_categories_request_instance = PostCategoriesRequest.from_json(json)
# print the JSON string representation of the object
print PostCategoriesRequest.to_json()

# convert the object into a dict
post_categories_request_dict = post_categories_request_instance.to_dict()
# create an instance of PostCategoriesRequest from a dict
post_categories_request_form_dict = post_categories_request.from_dict(post_categories_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


