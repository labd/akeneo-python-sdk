# AssetFamilies


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**AssetFamiliesEmbedded**](AssetFamiliesEmbedded.md) |  | [optional] 
**links** | [**ReferenceEntitiesLinks**](ReferenceEntitiesLinks.md) |  | [optional] 

## Example

```python
from akeneo.models.asset_families import AssetFamilies

# TODO update the JSON string below
json = "{}"
# create an instance of AssetFamilies from a JSON string
asset_families_instance = AssetFamilies.from_json(json)
# print the JSON string representation of the object
print AssetFamilies.to_json()

# convert the object into a dict
asset_families_dict = asset_families_instance.to_dict()
# create an instance of AssetFamilies from a dict
asset_families_form_dict = asset_families.from_dict(asset_families_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


