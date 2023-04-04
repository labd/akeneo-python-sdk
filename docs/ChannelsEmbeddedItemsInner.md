# ChannelsEmbeddedItemsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ProductsEmbeddedItemsInnerAllOfLinks**](ProductsEmbeddedItemsInnerAllOfLinks.md) |  | [optional] 
**code** | **str** | Channel code | 
**locales** | **List[str]** | Codes of activated locales for the channel | 
**currencies** | **List[str]** | Codes of activated currencies for the channel | 
**category_tree** | **str** | Code of the category tree linked to the channel | 
**conversion_units** | [**ChannelsEmbeddedItemsInnerAllOfConversionUnits**](ChannelsEmbeddedItemsInnerAllOfConversionUnits.md) |  | [optional] 
**labels** | [**ChannelsEmbeddedItemsInnerAllOfLabels**](ChannelsEmbeddedItemsInnerAllOfLabels.md) |  | [optional] 

## Example

```python
from akeneo.models.channels_embedded_items_inner import ChannelsEmbeddedItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelsEmbeddedItemsInner from a JSON string
channels_embedded_items_inner_instance = ChannelsEmbeddedItemsInner.from_json(json)
# print the JSON string representation of the object
print ChannelsEmbeddedItemsInner.to_json()

# convert the object into a dict
channels_embedded_items_inner_dict = channels_embedded_items_inner_instance.to_dict()
# create an instance of ChannelsEmbeddedItemsInner from a dict
channels_embedded_items_inner_form_dict = channels_embedded_items_inner.from_dict(channels_embedded_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


