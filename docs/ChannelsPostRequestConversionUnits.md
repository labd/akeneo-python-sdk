# ChannelsPostRequestConversionUnits

Units to which the given metric attributes should be converted when exporting products

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_code** | **str** | Conversion unit code used to convert the values of the attribute &#x60;attributeCode&#x60; when exporting via the channel | [optional] 

## Example

```python
from akeneo.models.channels_post_request_conversion_units import ChannelsPostRequestConversionUnits

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelsPostRequestConversionUnits from a JSON string
channels_post_request_conversion_units_instance = ChannelsPostRequestConversionUnits.from_json(json)
# print the JSON string representation of the object
print ChannelsPostRequestConversionUnits.to_json()

# convert the object into a dict
channels_post_request_conversion_units_dict = channels_post_request_conversion_units_instance.to_dict()
# create an instance of ChannelsPostRequestConversionUnits from a dict
channels_post_request_conversion_units_form_dict = channels_post_request_conversion_units.from_dict(channels_post_request_conversion_units_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


