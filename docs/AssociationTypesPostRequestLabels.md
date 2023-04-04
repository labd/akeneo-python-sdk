# AssociationTypesPostRequestLabels

Association type labels for each locale

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale_code** | **str** | Association type label for the locale &#x60;localeCode&#x60; | [optional] 

## Example

```python
from akeneo.models.association_types_post_request_labels import AssociationTypesPostRequestLabels

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationTypesPostRequestLabels from a JSON string
association_types_post_request_labels_instance = AssociationTypesPostRequestLabels.from_json(json)
# print the JSON string representation of the object
print AssociationTypesPostRequestLabels.to_json()

# convert the object into a dict
association_types_post_request_labels_dict = association_types_post_request_labels_instance.to_dict()
# create an instance of AssociationTypesPostRequestLabels from a dict
association_types_post_request_labels_form_dict = association_types_post_request_labels.from_dict(association_types_post_request_labels_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


