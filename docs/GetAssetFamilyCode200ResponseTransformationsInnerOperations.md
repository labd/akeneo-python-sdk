# GetAssetFamilyCode200ResponseTransformationsInnerOperations

The transformations that should be applied to your source file to generate the target file. More details <a href='/concepts/asset-manager.html#transformation-operations'>here</a>.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**parameters** | [**GetAssetFamilyCode200ResponseTransformationsInnerOperationsParameters**](GetAssetFamilyCode200ResponseTransformationsInnerOperationsParameters.md) |  | [optional] 

## Example

```python
from akeneo.models.get_asset_family_code200_response_transformations_inner_operations import GetAssetFamilyCode200ResponseTransformationsInnerOperations

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssetFamilyCode200ResponseTransformationsInnerOperations from a JSON string
get_asset_family_code200_response_transformations_inner_operations_instance = GetAssetFamilyCode200ResponseTransformationsInnerOperations.from_json(json)
# print the JSON string representation of the object
print GetAssetFamilyCode200ResponseTransformationsInnerOperations.to_json()

# convert the object into a dict
get_asset_family_code200_response_transformations_inner_operations_dict = get_asset_family_code200_response_transformations_inner_operations_instance.to_dict()
# create an instance of GetAssetFamilyCode200ResponseTransformationsInnerOperations from a dict
get_asset_family_code200_response_transformations_inner_operations_form_dict = get_asset_family_code200_response_transformations_inner_operations.from_dict(get_asset_family_code200_response_transformations_inner_operations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


