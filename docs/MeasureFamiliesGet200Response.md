# MeasureFamiliesGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Measure family code | 
**standard** | **str** | Measure family standard | [optional] 
**units** | [**List[MeasureFamiliesGet200ResponseUnitsInner]**](MeasureFamiliesGet200ResponseUnitsInner.md) | Family units | [optional] 

## Example

```python
from akeneo.models.measure_families_get200_response import MeasureFamiliesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MeasureFamiliesGet200Response from a JSON string
measure_families_get200_response_instance = MeasureFamiliesGet200Response.from_json(json)
# print the JSON string representation of the object
print MeasureFamiliesGet200Response.to_json()

# convert the object into a dict
measure_families_get200_response_dict = measure_families_get200_response_instance.to_dict()
# create an instance of MeasureFamiliesGet200Response from a dict
measure_families_get200_response_form_dict = measure_families_get200_response.from_dict(measure_families_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


