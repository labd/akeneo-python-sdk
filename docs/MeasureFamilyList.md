# MeasureFamilyList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ProductListAllOfLinks**](ProductListAllOfLinks.md) |  | [optional] 
**code** | **str** | Measure family code | 
**standard** | **str** | Measure family standard | [optional] 
**units** | [**List[MeasureFamilyListAllOfUnits]**](MeasureFamilyListAllOfUnits.md) | Family units | [optional] 

## Example

```python
from akeneo.models.measure_family_list import MeasureFamilyList

# TODO update the JSON string below
json = "{}"
# create an instance of MeasureFamilyList from a JSON string
measure_family_list_instance = MeasureFamilyList.from_json(json)
# print the JSON string representation of the object
print MeasureFamilyList.to_json()

# convert the object into a dict
measure_family_list_dict = measure_family_list_instance.to_dict()
# create an instance of MeasureFamilyList from a dict
measure_family_list_form_dict = measure_family_list.from_dict(measure_family_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


