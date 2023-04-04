# AttributeOptionsEmbeddedItemsInnerAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code of option | 
**attribute** | **str** | Code of attribute related to the attribute option | [optional] 
**sort_order** | **int** | Order of attribute option | [optional] 
**labels** | [**AttributeOptionsEmbeddedItemsInnerAllOfLabels**](AttributeOptionsEmbeddedItemsInnerAllOfLabels.md) |  | [optional] 

## Example

```python
from akeneo.models.attribute_options_embedded_items_inner_all_of import AttributeOptionsEmbeddedItemsInnerAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeOptionsEmbeddedItemsInnerAllOf from a JSON string
attribute_options_embedded_items_inner_all_of_instance = AttributeOptionsEmbeddedItemsInnerAllOf.from_json(json)
# print the JSON string representation of the object
print AttributeOptionsEmbeddedItemsInnerAllOf.to_json()

# convert the object into a dict
attribute_options_embedded_items_inner_all_of_dict = attribute_options_embedded_items_inner_all_of_instance.to_dict()
# create an instance of AttributeOptionsEmbeddedItemsInnerAllOf from a dict
attribute_options_embedded_items_inner_all_of_form_dict = attribute_options_embedded_items_inner_all_of.from_dict(attribute_options_embedded_items_inner_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


