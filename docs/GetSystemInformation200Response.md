# GetSystemInformation200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | Version of the PIM | [optional] 
**edition** | **str** | Edition of the PIM | [optional] 

## Example

```python
from akeneo.models.get_system_information200_response import GetSystemInformation200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSystemInformation200Response from a JSON string
get_system_information200_response_instance = GetSystemInformation200Response.from_json(json)
# print the JSON string representation of the object
print GetSystemInformation200Response.to_json()

# convert the object into a dict
get_system_information200_response_dict = get_system_information200_response_instance.to_dict()
# create an instance of GetSystemInformation200Response from a dict
get_system_information200_response_form_dict = get_system_information200_response.from_dict(get_system_information200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


