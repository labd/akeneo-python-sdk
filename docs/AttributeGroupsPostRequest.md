# AttributeGroupsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Attribute group code | 
**sort_order** | **int** | Attribute group order among other attribute groups | [optional] 
**attributes** | **List[str]** | Attribute codes that compose the attribute group | [optional] 
**labels** | [**AttributeGroupsPostRequestLabels**](AttributeGroupsPostRequestLabels.md) |  | [optional] 

## Example

```python
from akeneo.models.attribute_groups_post_request import AttributeGroupsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeGroupsPostRequest from a JSON string
attribute_groups_post_request_instance = AttributeGroupsPostRequest.from_json(json)
# print the JSON string representation of the object
print AttributeGroupsPostRequest.to_json()

# convert the object into a dict
attribute_groups_post_request_dict = attribute_groups_post_request_instance.to_dict()
# create an instance of AttributeGroupsPostRequest from a dict
attribute_groups_post_request_form_dict = attribute_groups_post_request.from_dict(attribute_groups_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


