# PatchReferenceEntityRecordsRequestInnerValuesAttributeCodeInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** | Channel code of the reference entity record value | [optional] 
**locale** | **str** | Locale code of the reference entity record value | [optional] 
**data** | **object** | Reference entity record value. See &lt;a href&#x3D;&#39;/concepts/reference-entities.html#the-data-format&#39;&gt;the &#x60;data&#x60; format&lt;/a&gt; section for more details. | [optional] 

## Example

```python
from openapi_client.models.patch_reference_entity_records_request_inner_values_attribute_code_inner import PatchReferenceEntityRecordsRequestInnerValuesAttributeCodeInner

# TODO update the JSON string below
json = "{}"
# create an instance of PatchReferenceEntityRecordsRequestInnerValuesAttributeCodeInner from a JSON string
patch_reference_entity_records_request_inner_values_attribute_code_inner_instance = PatchReferenceEntityRecordsRequestInnerValuesAttributeCodeInner.from_json(json)
# print the JSON string representation of the object
print PatchReferenceEntityRecordsRequestInnerValuesAttributeCodeInner.to_json()

# convert the object into a dict
patch_reference_entity_records_request_inner_values_attribute_code_inner_dict = patch_reference_entity_records_request_inner_values_attribute_code_inner_instance.to_dict()
# create an instance of PatchReferenceEntityRecordsRequestInnerValuesAttributeCodeInner from a dict
patch_reference_entity_records_request_inner_values_attribute_code_inner_form_dict = patch_reference_entity_records_request_inner_values_attribute_code_inner.from_dict(patch_reference_entity_records_request_inner_values_attribute_code_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


