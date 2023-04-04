# MeasureFamiliesEmbeddedItemsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ProductsEmbeddedItemsInnerAllOfLinks**](ProductsEmbeddedItemsInnerAllOfLinks.md) |  | [optional] 
**code** | **str** | Measure family code | 
**standard** | **str** | Measure family standard | [optional] 
**units** | [**List[MeasureFamiliesEmbeddedItemsInnerAllOfUnitsInner]**](MeasureFamiliesEmbeddedItemsInnerAllOfUnitsInner.md) | Family units | [optional] 

## Example

```python
from openapi_client.models.measure_families_embedded_items_inner import MeasureFamiliesEmbeddedItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MeasureFamiliesEmbeddedItemsInner from a JSON string
measure_families_embedded_items_inner_instance = MeasureFamiliesEmbeddedItemsInner.from_json(json)
# print the JSON string representation of the object
print MeasureFamiliesEmbeddedItemsInner.to_json()

# convert the object into a dict
measure_families_embedded_items_inner_dict = measure_families_embedded_items_inner_instance.to_dict()
# create an instance of MeasureFamiliesEmbeddedItemsInner from a dict
measure_families_embedded_items_inner_form_dict = measure_families_embedded_items_inner.from_dict(measure_families_embedded_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


