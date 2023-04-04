# AssetFamilyListAllOfOperations

The transformations that should be applied to your source file to generate the target file. More details <a href='/concepts/asset-manager.html#transformation-operations'>here</a>.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**parameters** | [**AssetFamilyListAllOfOperationsParameters**](AssetFamilyListAllOfOperationsParameters.md) |  | [optional] 

## Example

```python
from akeneo.models.asset_family_list_all_of_operations import AssetFamilyListAllOfOperations

# TODO update the JSON string below
json = "{}"
# create an instance of AssetFamilyListAllOfOperations from a JSON string
asset_family_list_all_of_operations_instance = AssetFamilyListAllOfOperations.from_json(json)
# print the JSON string representation of the object
print AssetFamilyListAllOfOperations.to_json()

# convert the object into a dict
asset_family_list_all_of_operations_dict = asset_family_list_all_of_operations_instance.to_dict()
# create an instance of AssetFamilyListAllOfOperations from a dict
asset_family_list_all_of_operations_form_dict = asset_family_list_all_of_operations.from_dict(asset_family_list_all_of_operations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


