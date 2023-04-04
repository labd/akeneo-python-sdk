# ChannelListAllOfConversionUnits

Units to which the given metric attributes should be converted when exporting products

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_code** | **str** | Conversion unit code used to convert the values of the attribute &#x60;attributeCode&#x60; when exporting via the channel | [optional] 

## Example

```python
from openapi_client.models.channel_list_all_of_conversion_units import ChannelListAllOfConversionUnits

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelListAllOfConversionUnits from a JSON string
channel_list_all_of_conversion_units_instance = ChannelListAllOfConversionUnits.from_json(json)
# print the JSON string representation of the object
print ChannelListAllOfConversionUnits.to_json()

# convert the object into a dict
channel_list_all_of_conversion_units_dict = channel_list_all_of_conversion_units_instance.to_dict()
# create an instance of ChannelListAllOfConversionUnits from a dict
channel_list_all_of_conversion_units_form_dict = channel_list_all_of_conversion_units.from_dict(channel_list_all_of_conversion_units_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


