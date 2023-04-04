# GetProducts401Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | HTTP status code | [optional] 
**message** | **str** | Message explaining the error | [optional] 

## Example

```python
from akeneo.models.get_products401_response import GetProducts401Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetProducts401Response from a JSON string
get_products401_response_instance = GetProducts401Response.from_json(json)
# print the JSON string representation of the object
print GetProducts401Response.to_json()

# convert the object into a dict
get_products401_response_dict = get_products401_response_instance.to_dict()
# create an instance of GetProducts401Response from a dict
get_products401_response_form_dict = get_products401_response.from_dict(get_products401_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


