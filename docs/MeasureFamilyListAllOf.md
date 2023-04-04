# MeasureFamilyListAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Measure family code | 
**standard** | **str** | Measure family standard | [optional] 
**units** | [**List[MeasureFamilyListAllOfUnits]**](MeasureFamilyListAllOfUnits.md) | Family units | [optional] 

## Example

```python
from openapi_client.models.measure_family_list_all_of import MeasureFamilyListAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of MeasureFamilyListAllOf from a JSON string
measure_family_list_all_of_instance = MeasureFamilyListAllOf.from_json(json)
# print the JSON string representation of the object
print MeasureFamilyListAllOf.to_json()

# convert the object into a dict
measure_family_list_all_of_dict = measure_family_list_all_of_instance.to_dict()
# create an instance of MeasureFamilyListAllOf from a dict
measure_family_list_all_of_form_dict = measure_family_list_all_of.from_dict(measure_family_list_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


