# CategoryList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ProductListAllOfLinks**](ProductListAllOfLinks.md) |  | [optional] 
**code** | **str** | Category code | 
**parent** | **str** | Category code of the parent&#39;s category | [optional] [default to 'null']
**updated** | **str** | Date of the last update | [optional] 
**position** | **int** | Position of the category in its level, start from 1 (only available since the 7.0 version and when query parameter \&quot;with_position\&quot; is set to \&quot;true\&quot;) | [optional] 
**labels** | [**CategoryListAllOfLabels**](CategoryListAllOfLabels.md) |  | [optional] 
**values** | [**CategoryListAllOfValues**](CategoryListAllOfValues.md) |  | [optional] 

## Example

```python
from openapi_client.models.category_list import CategoryList

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryList from a JSON string
category_list_instance = CategoryList.from_json(json)
# print the JSON string representation of the object
print CategoryList.to_json()

# convert the object into a dict
category_list_dict = category_list_instance.to_dict()
# create an instance of CategoryList from a dict
category_list_form_dict = category_list.from_dict(category_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


