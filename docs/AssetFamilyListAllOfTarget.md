# AssetFamilyListAllOfTarget

The attribute value in which the PIM will generate the new transformed file, aka the target file. More details <a href='/concepts/asset-manager.html#target-file'>here</a>.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** |  | 
**channel** | **str** |  | 
**locale** | **str** |  | 

## Example

```python
from akeneo.models.asset_family_list_all_of_target import AssetFamilyListAllOfTarget

# TODO update the JSON string below
json = "{}"
# create an instance of AssetFamilyListAllOfTarget from a JSON string
asset_family_list_all_of_target_instance = AssetFamilyListAllOfTarget.from_json(json)
# print the JSON string representation of the object
print AssetFamilyListAllOfTarget.to_json()

# convert the object into a dict
asset_family_list_all_of_target_dict = asset_family_list_all_of_target_instance.to_dict()
# create an instance of AssetFamilyListAllOfTarget from a dict
asset_family_list_all_of_target_form_dict = asset_family_list_all_of_target.from_dict(asset_family_list_all_of_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


