# ReferenceEntityList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ReferenceEntityListAllOfLinks**](ReferenceEntityListAllOfLinks.md) |  | [optional] 
**code** | **str** | Reference entity code | 
**labels** | [**ReferenceEntityAllOf1Labels**](ReferenceEntityAllOf1Labels.md) |  | [optional] 
**image** | **str** | Code of the reference entity image | [optional] [default to 'null']

## Example

```python
from akeneo.models.reference_entity_list import ReferenceEntityList

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceEntityList from a JSON string
reference_entity_list_instance = ReferenceEntityList.from_json(json)
# print the JSON string representation of the object
print ReferenceEntityList.to_json()

# convert the object into a dict
reference_entity_list_dict = reference_entity_list_instance.to_dict()
# create an instance of ReferenceEntityList from a dict
reference_entity_list_form_dict = reference_entity_list.from_dict(reference_entity_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


