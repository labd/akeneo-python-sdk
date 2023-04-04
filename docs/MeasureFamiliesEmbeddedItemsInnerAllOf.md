# MeasureFamiliesEmbeddedItemsInnerAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Measure family code | 
**standard** | **str** | Measure family standard | [optional] 
**units** | [**List[MeasureFamiliesEmbeddedItemsInnerAllOfUnitsInner]**](MeasureFamiliesEmbeddedItemsInnerAllOfUnitsInner.md) | Family units | [optional] 

## Example

```python
from akeneo.models.measure_families_embedded_items_inner_all_of import MeasureFamiliesEmbeddedItemsInnerAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of MeasureFamiliesEmbeddedItemsInnerAllOf from a JSON string
measure_families_embedded_items_inner_all_of_instance = MeasureFamiliesEmbeddedItemsInnerAllOf.from_json(json)
# print the JSON string representation of the object
print MeasureFamiliesEmbeddedItemsInnerAllOf.to_json()

# convert the object into a dict
measure_families_embedded_items_inner_all_of_dict = measure_families_embedded_items_inner_all_of_instance.to_dict()
# create an instance of MeasureFamiliesEmbeddedItemsInnerAllOf from a dict
measure_families_embedded_items_inner_all_of_form_dict = measure_families_embedded_items_inner_all_of.from_dict(measure_families_embedded_items_inner_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


