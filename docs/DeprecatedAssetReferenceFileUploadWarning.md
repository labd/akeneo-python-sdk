# DeprecatedAssetReferenceFileUploadWarning


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message explaining the warning | [optional] 
**errors** | [**List[PostReferenceFilesLocaleCode201ResponseErrorsInner]**](PostReferenceFilesLocaleCode201ResponseErrorsInner.md) |  | [optional] 

## Example

```python
from akeneo.models.deprecated_asset_reference_file_upload_warning import DeprecatedAssetReferenceFileUploadWarning

# TODO update the JSON string below
json = "{}"
# create an instance of DeprecatedAssetReferenceFileUploadWarning from a JSON string
deprecated_asset_reference_file_upload_warning_instance = DeprecatedAssetReferenceFileUploadWarning.from_json(json)
# print the JSON string representation of the object
print DeprecatedAssetReferenceFileUploadWarning.to_json()

# convert the object into a dict
deprecated_asset_reference_file_upload_warning_dict = deprecated_asset_reference_file_upload_warning_instance.to_dict()
# create an instance of DeprecatedAssetReferenceFileUploadWarning from a dict
deprecated_asset_reference_file_upload_warning_form_dict = deprecated_asset_reference_file_upload_warning.from_dict(deprecated_asset_reference_file_upload_warning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


