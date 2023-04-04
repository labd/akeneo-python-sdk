# ProductsEmbeddedItemsInnerAllOf1ValuesValueInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | &lt;a href&#x3D;&#39;api-reference.html#Channel&#39;&gt;Channel&lt;/a&gt; code of the product value | [optional] 
**locale** | **str** | &lt;a href&#x3D;&#39;api-reference.html#Locale&#39;&gt;Locale&lt;/a&gt; code of the product value | [optional] 
**data** | **object** | Product value. See &lt;a href&#x3D;&#39;/concepts/products.html#the-data-format&#39;&gt;the &#x60;data&#x60; format&lt;/a&gt; section for more details. | [optional] 
**linked_data** | [**ProductsEmbeddedItemsInnerAllOf1ValuesValueInnerLinkedData**](ProductsEmbeddedItemsInnerAllOf1ValuesValueInnerLinkedData.md) |  | [optional] 

## Example

```python
from openapi_client.models.products_embedded_items_inner_all_of1_values_value_inner import ProductsEmbeddedItemsInnerAllOf1ValuesValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProductsEmbeddedItemsInnerAllOf1ValuesValueInner from a JSON string
products_embedded_items_inner_all_of1_values_value_inner_instance = ProductsEmbeddedItemsInnerAllOf1ValuesValueInner.from_json(json)
# print the JSON string representation of the object
print ProductsEmbeddedItemsInnerAllOf1ValuesValueInner.to_json()

# convert the object into a dict
products_embedded_items_inner_all_of1_values_value_inner_dict = products_embedded_items_inner_all_of1_values_value_inner_instance.to_dict()
# create an instance of ProductsEmbeddedItemsInnerAllOf1ValuesValueInner from a dict
products_embedded_items_inner_all_of1_values_value_inner_form_dict = products_embedded_items_inner_all_of1_values_value_inner.from_dict(products_embedded_items_inner_all_of1_values_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


