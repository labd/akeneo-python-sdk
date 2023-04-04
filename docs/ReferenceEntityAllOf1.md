# ReferenceEntityAllOf1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Reference entity code | 
**labels** | [**ReferenceEntityAllOf1Labels**](ReferenceEntityAllOf1Labels.md) |  | [optional] 
**image** | **str** | Code of the reference entity image | [optional] [default to 'null']

## Example

```python
from openapi_client.models.reference_entity_all_of1 import ReferenceEntityAllOf1

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceEntityAllOf1 from a JSON string
reference_entity_all_of1_instance = ReferenceEntityAllOf1.from_json(json)
# print the JSON string representation of the object
print ReferenceEntityAllOf1.to_json()

# convert the object into a dict
reference_entity_all_of1_dict = reference_entity_all_of1_instance.to_dict()
# create an instance of ReferenceEntityAllOf1 from a dict
reference_entity_all_of1_form_dict = reference_entity_all_of1.from_dict(reference_entity_all_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


