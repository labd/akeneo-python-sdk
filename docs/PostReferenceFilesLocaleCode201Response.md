# PostReferenceFilesLocaleCode201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message explaining the warning | [optional] 
**errors** | [**List[PostReferenceFilesLocaleCode201ResponseErrorsInner]**](PostReferenceFilesLocaleCode201ResponseErrorsInner.md) |  | [optional] 

## Example

```python
from akeneo.models.post_reference_files_locale_code201_response import PostReferenceFilesLocaleCode201Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostReferenceFilesLocaleCode201Response from a JSON string
post_reference_files_locale_code201_response_instance = PostReferenceFilesLocaleCode201Response.from_json(json)
# print the JSON string representation of the object
print PostReferenceFilesLocaleCode201Response.to_json()

# convert the object into a dict
post_reference_files_locale_code201_response_dict = post_reference_files_locale_code201_response_instance.to_dict()
# create an instance of PostReferenceFilesLocaleCode201Response from a dict
post_reference_files_locale_code201_response_form_dict = post_reference_files_locale_code201_response.from_dict(post_reference_files_locale_code201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


