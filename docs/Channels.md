# Channels


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**ChannelsEmbedded**](ChannelsEmbedded.md) |  | [optional] 
**links** | [**ProductsLinks**](ProductsLinks.md) |  | [optional] 
**current_page** | **int** | Current page number | [optional] 

## Example

```python
from akeneo.models.channels import Channels

# TODO update the JSON string below
json = "{}"
# create an instance of Channels from a JSON string
channels_instance = Channels.from_json(json)
# print the JSON string representation of the object
print Channels.to_json()

# convert the object into a dict
channels_dict = channels_instance.to_dict()
# create an instance of Channels from a dict
channels_form_dict = channels.from_dict(channels_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


