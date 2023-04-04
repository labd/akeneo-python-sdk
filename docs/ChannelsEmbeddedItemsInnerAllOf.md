# ChannelsEmbeddedItemsInnerAllOf


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
from openapi_client.models.channels_embedded_items_inner_all_of import ChannelsEmbeddedItemsInnerAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelsEmbeddedItemsInnerAllOf from a JSON string
channels_embedded_items_inner_all_of_instance = ChannelsEmbeddedItemsInnerAllOf.from_json(json)
# print the JSON string representation of the object
print ChannelsEmbeddedItemsInnerAllOf.to_json()

# convert the object into a dict
channels_embedded_items_inner_all_of_dict = channels_embedded_items_inner_all_of_instance.to_dict()
# create an instance of ChannelsEmbeddedItemsInnerAllOf from a dict
channels_embedded_items_inner_all_of_form_dict = channels_embedded_items_inner_all_of.from_dict(channels_embedded_items_inner_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


