# SeveralChannelsPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Channel code | 
**locales** | **List[str]** | Codes of activated locales for the channel | 
**currencies** | **List[str]** | Codes of activated currencies for the channel | 
**category_tree** | **str** | Code of the category tree linked to the channel | 
**conversion_units** | [**ChannelsEmbeddedItemsInnerAllOfConversionUnits**](ChannelsEmbeddedItemsInnerAllOfConversionUnits.md) |  | [optional] 
**labels** | [**ChannelsEmbeddedItemsInnerAllOfLabels**](ChannelsEmbeddedItemsInnerAllOfLabels.md) |  | [optional] 

## Example

```python
from openapi_client.models.several_channels_patch_request import SeveralChannelsPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SeveralChannelsPatchRequest from a JSON string
several_channels_patch_request_instance = SeveralChannelsPatchRequest.from_json(json)
# print the JSON string representation of the object
print SeveralChannelsPatchRequest.to_json()

# convert the object into a dict
several_channels_patch_request_dict = several_channels_patch_request_instance.to_dict()
# create an instance of SeveralChannelsPatchRequest from a dict
several_channels_patch_request_form_dict = several_channels_patch_request.from_dict(several_channels_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


