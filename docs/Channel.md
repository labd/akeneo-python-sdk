# Channel


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
from openapi_client.models.channel import Channel

# TODO update the JSON string below
json = "{}"
# create an instance of Channel from a JSON string
channel_instance = Channel.from_json(json)
# print the JSON string representation of the object
print Channel.to_json()

# convert the object into a dict
channel_dict = channel_instance.to_dict()
# create an instance of Channel from a dict
channel_form_dict = channel.from_dict(channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


