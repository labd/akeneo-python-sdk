# ReferenceEntityRecordListAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code of the record | 
**values** | **Dict[str, List[object]]** | Record attributes values, see &lt;a href&#x3D;&#39;/concepts/reference-entities.html#focus-on-the-reference-entity-record-values&#39;&gt;Reference entity record values&lt;/a&gt; section for more details | [optional] 
**created** | **str** | Date of creation. | [optional] [default to 'null']
**updated** | **str** | Date of the last update. | [optional] [default to 'null']

## Example

```python
from akeneo.models.reference_entity_record_list_all_of import ReferenceEntityRecordListAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceEntityRecordListAllOf from a JSON string
reference_entity_record_list_all_of_instance = ReferenceEntityRecordListAllOf.from_json(json)
# print the JSON string representation of the object
print ReferenceEntityRecordListAllOf.to_json()

# convert the object into a dict
reference_entity_record_list_all_of_dict = reference_entity_record_list_all_of_instance.to_dict()
# create an instance of ReferenceEntityRecordListAllOf from a dict
reference_entity_record_list_all_of_form_dict = reference_entity_record_list_all_of.from_dict(reference_entity_record_list_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


