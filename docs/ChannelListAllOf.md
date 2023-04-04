# ChannelListAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Channel code | 
**locales** | **List[str]** | Codes of activated locales for the channel | 
**currencies** | **List[str]** | Codes of activated currencies for the channel | 
**category_tree** | **str** | Code of the category tree linked to the channel | 
**conversion_units** | [**ChannelListAllOfConversionUnits**](ChannelListAllOfConversionUnits.md) |  | [optional] 
**labels** | [**ChannelListAllOfLabels**](ChannelListAllOfLabels.md) |  | [optional] 

## Example

```python
from openapi_client.models.channel_list_all_of import ChannelListAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelListAllOf from a JSON string
channel_list_all_of_instance = ChannelListAllOf.from_json(json)
# print the JSON string representation of the object
print ChannelListAllOf.to_json()

# convert the object into a dict
channel_list_all_of_dict = channel_list_all_of_instance.to_dict()
# create an instance of ChannelListAllOf from a dict
channel_list_all_of_form_dict = channel_list_all_of.from_dict(channel_list_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


