# ReferenceEntitiesEmbeddedItemsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ReferenceEntitiesEmbeddedItemsInnerAllOfLinks**](ReferenceEntitiesEmbeddedItemsInnerAllOfLinks.md) |  | [optional] 
**code** | **str** | Reference entity code | 
**labels** | [**ReferenceEntitiesEmbeddedItemsInnerAllOf1Labels**](ReferenceEntitiesEmbeddedItemsInnerAllOf1Labels.md) |  | [optional] 
**image** | **str** | Code of the reference entity image | [optional] [default to 'null']

## Example

```python
from openapi_client.models.reference_entities_embedded_items_inner import ReferenceEntitiesEmbeddedItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceEntitiesEmbeddedItemsInner from a JSON string
reference_entities_embedded_items_inner_instance = ReferenceEntitiesEmbeddedItemsInner.from_json(json)
# print the JSON string representation of the object
print ReferenceEntitiesEmbeddedItemsInner.to_json()

# convert the object into a dict
reference_entities_embedded_items_inner_dict = reference_entities_embedded_items_inner_instance.to_dict()
# create an instance of ReferenceEntitiesEmbeddedItemsInner from a dict
reference_entities_embedded_items_inner_form_dict = reference_entities_embedded_items_inner.from_dict(reference_entities_embedded_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


