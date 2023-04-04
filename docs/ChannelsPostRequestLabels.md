# ChannelsPostRequestLabels

Channel labels for each locale

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale_code** | **str** | Channel label for the locale &#x60;localeCode&#x60; | [optional] 

## Example

```python
from akeneo.models.channels_post_request_labels import ChannelsPostRequestLabels

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelsPostRequestLabels from a JSON string
channels_post_request_labels_instance = ChannelsPostRequestLabels.from_json(json)
# print the JSON string representation of the object
print ChannelsPostRequestLabels.to_json()

# convert the object into a dict
channels_post_request_labels_dict = channels_post_request_labels_instance.to_dict()
# create an instance of ChannelsPostRequestLabels from a dict
channels_post_request_labels_form_dict = channels_post_request_labels.from_dict(channels_post_request_labels_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


