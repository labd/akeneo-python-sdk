# ChannelList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ProductListAllOfLinks**](ProductListAllOfLinks.md) |  | [optional] 
**code** | **str** | Channel code | 
**locales** | **List[str]** | Codes of activated locales for the channel | 
**currencies** | **List[str]** | Codes of activated currencies for the channel | 
**category_tree** | **str** | Code of the category tree linked to the channel | 
**conversion_units** | [**ChannelListAllOfConversionUnits**](ChannelListAllOfConversionUnits.md) |  | [optional] 
**labels** | [**ChannelListAllOfLabels**](ChannelListAllOfLabels.md) |  | [optional] 

## Example

```python
from akeneo.models.channel_list import ChannelList

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelList from a JSON string
channel_list_instance = ChannelList.from_json(json)
# print the JSON string representation of the object
print ChannelList.to_json()

# convert the object into a dict
channel_list_dict = channel_list_instance.to_dict()
# create an instance of ChannelList from a dict
channel_list_form_dict = channel_list.from_dict(channel_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


