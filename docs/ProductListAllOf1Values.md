# ProductListAllOf1Values

Product attributes values, see <a href='/concepts/products.html#focus-on-the-product-values'>Product values</a> section for more details

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_code** | [**List[ProductListAllOf1ValuesAttributeCode]**](ProductListAllOf1ValuesAttributeCode.md) |  | [optional] 

## Example

```python
from akeneo.models.product_list_all_of1_values import ProductListAllOf1Values

# TODO update the JSON string below
json = "{}"
# create an instance of ProductListAllOf1Values from a JSON string
product_list_all_of1_values_instance = ProductListAllOf1Values.from_json(json)
# print the JSON string representation of the object
print ProductListAllOf1Values.to_json()

# convert the object into a dict
product_list_all_of1_values_dict = product_list_all_of1_values_instance.to_dict()
# create an instance of ProductListAllOf1Values from a dict
product_list_all_of1_values_form_dict = product_list_all_of1_values.from_dict(product_list_all_of1_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


