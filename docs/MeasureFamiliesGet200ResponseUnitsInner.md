# MeasureFamiliesGet200ResponseUnitsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Measure code | [optional] 
**convert** | **object** | Mathematic operation to convert the unit into the standard unit | [optional] 
**symbol** | **str** | Measure symbol | [optional] 

## Example

```python
from akeneo.models.measure_families_get200_response_units_inner import MeasureFamiliesGet200ResponseUnitsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MeasureFamiliesGet200ResponseUnitsInner from a JSON string
measure_families_get200_response_units_inner_instance = MeasureFamiliesGet200ResponseUnitsInner.from_json(json)
# print the JSON string representation of the object
print MeasureFamiliesGet200ResponseUnitsInner.to_json()

# convert the object into a dict
measure_families_get200_response_units_inner_dict = measure_families_get200_response_units_inner_instance.to_dict()
# create an instance of MeasureFamiliesGet200ResponseUnitsInner from a dict
measure_families_get200_response_units_inner_form_dict = measure_families_get200_response_units_inner.from_dict(measure_families_get200_response_units_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


