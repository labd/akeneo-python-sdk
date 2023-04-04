# PostFamiliesRequestAttributeRequirements

Attributes codes of the family that are required for the completeness calculation for each channel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_code** | **List[str]** |  | [optional] 

## Example

```python
from akeneo.models.post_families_request_attribute_requirements import PostFamiliesRequestAttributeRequirements

# TODO update the JSON string below
json = "{}"
# create an instance of PostFamiliesRequestAttributeRequirements from a JSON string
post_families_request_attribute_requirements_instance = PostFamiliesRequestAttributeRequirements.from_json(json)
# print the JSON string representation of the object
print PostFamiliesRequestAttributeRequirements.to_json()

# convert the object into a dict
post_families_request_attribute_requirements_dict = post_families_request_attribute_requirements_instance.to_dict()
# create an instance of PostFamiliesRequestAttributeRequirements from a dict
post_families_request_attribute_requirements_form_dict = post_families_request_attribute_requirements.from_dict(post_families_request_attribute_requirements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


