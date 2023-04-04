# AssetFamilyListAllOfSource

The attribute value in which is stored the media file you want to use as the source file for your transformation. More details <a href='/concepts/asset-manager.html#source-file'>here</a>.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** |  | 
**channel** | **str** |  | 
**locale** | **str** |  | 

## Example

```python
from openapi_client.models.asset_family_list_all_of_source import AssetFamilyListAllOfSource

# TODO update the JSON string below
json = "{}"
# create an instance of AssetFamilyListAllOfSource from a JSON string
asset_family_list_all_of_source_instance = AssetFamilyListAllOfSource.from_json(json)
# print the JSON string representation of the object
print AssetFamilyListAllOfSource.to_json()

# convert the object into a dict
asset_family_list_all_of_source_dict = asset_family_list_all_of_source_instance.to_dict()
# create an instance of AssetFamilyListAllOfSource from a dict
asset_family_list_all_of_source_form_dict = asset_family_list_all_of_source.from_dict(asset_family_list_all_of_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


