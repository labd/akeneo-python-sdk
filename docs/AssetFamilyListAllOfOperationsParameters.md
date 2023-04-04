# AssetFamilyListAllOfOperationsParameters


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**colorspace** | **str** |  | [optional] 
**width** | **int** |  | [optional] 
**height** | **int** |  | [optional] 
**ratio** | **int** |  | [optional] 
**resolution_unit** | **str** |  | [optional] 
**resolution_x** | **int** |  | [optional] 
**resolution_y** | **int** |  | [optional] 
**quality** | **int** |  | [optional] 

## Example

```python
from akeneo.models.asset_family_list_all_of_operations_parameters import AssetFamilyListAllOfOperationsParameters

# TODO update the JSON string below
json = "{}"
# create an instance of AssetFamilyListAllOfOperationsParameters from a JSON string
asset_family_list_all_of_operations_parameters_instance = AssetFamilyListAllOfOperationsParameters.from_json(json)
# print the JSON string representation of the object
print AssetFamilyListAllOfOperationsParameters.to_json()

# convert the object into a dict
asset_family_list_all_of_operations_parameters_dict = asset_family_list_all_of_operations_parameters_instance.to_dict()
# create an instance of AssetFamilyListAllOfOperationsParameters from a dict
asset_family_list_all_of_operations_parameters_form_dict = asset_family_list_all_of_operations_parameters.from_dict(asset_family_list_all_of_operations_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


