# ProductListAllOf1ValuesLinkedData

Object containing labels of attribute options (only available since the 5.0 and when query parameter \"with_attribute_options\" is set to \"true\"). See <a href='/concepts/products.html#the-linked_data-format'>the `linked_data` format</a> section for more details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**labels** | **object** |  | [optional] 

## Example

```python
from akeneo.models.product_list_all_of1_values_linked_data import ProductListAllOf1ValuesLinkedData

# TODO update the JSON string below
json = "{}"
# create an instance of ProductListAllOf1ValuesLinkedData from a JSON string
product_list_all_of1_values_linked_data_instance = ProductListAllOf1ValuesLinkedData.from_json(json)
# print the JSON string representation of the object
print ProductListAllOf1ValuesLinkedData.to_json()

# convert the object into a dict
product_list_all_of1_values_linked_data_dict = product_list_all_of1_values_linked_data_instance.to_dict()
# create an instance of ProductListAllOf1ValuesLinkedData from a dict
product_list_all_of1_values_linked_data_form_dict = product_list_all_of1_values_linked_data.from_dict(product_list_all_of1_values_linked_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


