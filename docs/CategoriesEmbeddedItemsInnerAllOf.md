# CategoriesEmbeddedItemsInnerAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Category code | 
**parent** | **str** | Category code of the parent&#39;s category | [optional] [default to 'null']
**updated** | **str** | Date of the last update | [optional] 
**position** | **int** | Position of the category in its level, start from 1 (only available since the 7.0 version and when query parameter \&quot;with_position\&quot; is set to \&quot;true\&quot;) | [optional] 
**labels** | [**CategoriesEmbeddedItemsInnerAllOfLabels**](CategoriesEmbeddedItemsInnerAllOfLabels.md) |  | [optional] 
**values** | [**CategoriesEmbeddedItemsInnerAllOfValues**](CategoriesEmbeddedItemsInnerAllOfValues.md) |  | [optional] 

## Example

```python
from openapi_client.models.categories_embedded_items_inner_all_of import CategoriesEmbeddedItemsInnerAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of CategoriesEmbeddedItemsInnerAllOf from a JSON string
categories_embedded_items_inner_all_of_instance = CategoriesEmbeddedItemsInnerAllOf.from_json(json)
# print the JSON string representation of the object
print CategoriesEmbeddedItemsInnerAllOf.to_json()

# convert the object into a dict
categories_embedded_items_inner_all_of_dict = categories_embedded_items_inner_all_of_instance.to_dict()
# create an instance of CategoriesEmbeddedItemsInnerAllOf from a dict
categories_embedded_items_inner_all_of_form_dict = categories_embedded_items_inner_all_of.from_dict(categories_embedded_items_inner_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


