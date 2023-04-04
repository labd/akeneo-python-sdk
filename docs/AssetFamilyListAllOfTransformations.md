# AssetFamilyListAllOfTransformations


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The name of the transformation | 
**filename_suffix** | **str** | The suffix that will be appended to the source filename to generate the target filename. More details &lt;a href&#x3D;&#39;/concepts/asset-manager.html#target-filename&#39;&gt;here&lt;/a&gt;. | [optional] 
**filename_prefix** | **str** | The prefix that will be prepended to the source filename to generate the target filename. More details &lt;a href&#x3D;&#39;/concepts/asset-manager.html#target-filename&#39;&gt;here&lt;/a&gt;. | [optional] 
**source** | [**AssetFamilyListAllOfSource**](AssetFamilyListAllOfSource.md) |  | 
**target** | [**AssetFamilyListAllOfTarget**](AssetFamilyListAllOfTarget.md) |  | 
**operations** | [**AssetFamilyListAllOfOperations**](AssetFamilyListAllOfOperations.md) |  | 

## Example

```python
from akeneo.models.asset_family_list_all_of_transformations import AssetFamilyListAllOfTransformations

# TODO update the JSON string below
json = "{}"
# create an instance of AssetFamilyListAllOfTransformations from a JSON string
asset_family_list_all_of_transformations_instance = AssetFamilyListAllOfTransformations.from_json(json)
# print the JSON string representation of the object
print AssetFamilyListAllOfTransformations.to_json()

# convert the object into a dict
asset_family_list_all_of_transformations_dict = asset_family_list_all_of_transformations_instance.to_dict()
# create an instance of AssetFamilyListAllOfTransformations from a dict
asset_family_list_all_of_transformations_form_dict = asset_family_list_all_of_transformations.from_dict(asset_family_list_all_of_transformations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


