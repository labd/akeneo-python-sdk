# PAMAssets


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**PAMAssetsEmbedded**](PAMAssetsEmbedded.md) |  | [optional] 
**links** | [**ProductsLinks**](ProductsLinks.md) |  | [optional] 
**current_page** | **int** | Current page number | [optional] 

## Example

```python
from akeneo.models.pam_assets import PAMAssets

# TODO update the JSON string below
json = "{}"
# create an instance of PAMAssets from a JSON string
pam_assets_instance = PAMAssets.from_json(json)
# print the JSON string representation of the object
print PAMAssets.to_json()

# convert the object into a dict
pam_assets_dict = pam_assets_instance.to_dict()
# create an instance of PAMAssets from a dict
pam_assets_form_dict = pam_assets.from_dict(pam_assets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


