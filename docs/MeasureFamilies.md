# MeasureFamilies


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**MeasureFamiliesEmbedded**](MeasureFamiliesEmbedded.md) |  | [optional] 
**links** | [**ProductsLinks**](ProductsLinks.md) |  | [optional] 
**current_page** | **int** | Current page number | [optional] 

## Example

```python
from akeneo.models.measure_families import MeasureFamilies

# TODO update the JSON string below
json = "{}"
# create an instance of MeasureFamilies from a JSON string
measure_families_instance = MeasureFamilies.from_json(json)
# print the JSON string representation of the object
print MeasureFamilies.to_json()

# convert the object into a dict
measure_families_dict = measure_families_instance.to_dict()
# create an instance of MeasureFamilies from a dict
measure_families_form_dict = measure_families.from_dict(measure_families_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


