# DeprecatedAssetTagList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ProductListAllOfLinks**](ProductListAllOfLinks.md) |  | [optional] 
**code** | **str** | PAM asset tag code | 

## Example

```python
from akeneo.models.deprecated_asset_tag_list import DeprecatedAssetTagList

# TODO update the JSON string below
json = "{}"
# create an instance of DeprecatedAssetTagList from a JSON string
deprecated_asset_tag_list_instance = DeprecatedAssetTagList.from_json(json)
# print the JSON string representation of the object
print DeprecatedAssetTagList.to_json()

# convert the object into a dict
deprecated_asset_tag_list_dict = deprecated_asset_tag_list_instance.to_dict()
# create an instance of DeprecatedAssetTagList from a dict
deprecated_asset_tag_list_form_dict = deprecated_asset_tag_list.from_dict(deprecated_asset_tag_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


