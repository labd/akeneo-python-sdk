# PostFamiliesRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Family code | 
**attribute_as_label** | **str** | Attribute code used as label | 
**attribute_as_image** | **str** | Attribute code used as the main picture in the user interface (only since v2.0) | [optional] [default to 'null']
**attributes** | **List[str]** | Attributes codes that compose the family | [optional] 
**attribute_requirements** | [**PostFamiliesRequestAttributeRequirements**](PostFamiliesRequestAttributeRequirements.md) |  | [optional] 
**labels** | [**PostFamiliesRequestLabels**](PostFamiliesRequestLabels.md) |  | [optional] 

## Example

```python
from akeneo.models.post_families_request import PostFamiliesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostFamiliesRequest from a JSON string
post_families_request_instance = PostFamiliesRequest.from_json(json)
# print the JSON string representation of the object
print PostFamiliesRequest.to_json()

# convert the object into a dict
post_families_request_dict = post_families_request_instance.to_dict()
# create an instance of PostFamiliesRequest from a dict
post_families_request_form_dict = post_families_request.from_dict(post_families_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


