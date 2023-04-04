# ProductListAllOf1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Product UUID | [optional] 
**identifier** | **str** | Product identifier, i.e. the value of the only &#x60;pim_catalog_identifier&#x60; attribute | 
**enabled** | **bool** | Whether the product is enabled | [optional] [default to True]
**family** | **str** | &lt;a href&#x3D;&#39;api-reference.html#Family&#39;&gt;Family&lt;/a&gt; code from which the product inherits its attributes and attributes requirements. | [optional] [default to 'null only in the case of a non variant product']
**categories** | **List[str]** | Codes of the &lt;a href&#x3D;&#39;api-reference.html#Category&#39;&gt;categories&lt;/a&gt; in which the product is classified | [optional] 
**groups** | **List[str]** | Codes of the groups to which the product belong | [optional] 
**parent** | **str** | Code of the parent &lt;a href&#x3D;&#39;api-reference.html#Productmodel&#39;&gt;product model&lt;/a&gt; when the product is a variant (only available since the 2.0). This parent can be modified since the 2.3. | [optional] [default to 'null']
**values** | **Dict[str, List[object]]** | Product attributes values, see &lt;a href&#x3D;&#39;/concepts/products.html#focus-on-the-product-values&#39;&gt;Product values&lt;/a&gt; section for more details | [optional] 
**associations** | [**ProductListAllOf1Associations**](ProductListAllOf1Associations.md) |  | [optional] 
**quantified_associations** | [**ProductListAllOf1QuantifiedAssociations**](ProductListAllOf1QuantifiedAssociations.md) |  | [optional] 
**created** | **str** | Date of creation | [optional] 
**updated** | **str** | Date of the last update | [optional] 
**metadata** | [**ProductListAllOf1Metadata**](ProductListAllOf1Metadata.md) |  | [optional] 
**quality_scores** | **object** | Product quality scores for each channel/locale combination (only available since the 5.0 and when the \&quot;with_quality_scores\&quot; query parameter is set to \&quot;true\&quot;) | [optional] 
**completenesses** | [**List[ProductListAllOf1Completenesses]**](ProductListAllOf1Completenesses.md) | Product completenesses for each channel/locale combination (only available since the 7.0 version, and when the \&quot;with_completenesses\&quot; query parameter is set to \&quot;true\&quot;) | [optional] 

## Example

```python
from akeneo.models.product_list_all_of1 import ProductListAllOf1

# TODO update the JSON string below
json = "{}"
# create an instance of ProductListAllOf1 from a JSON string
product_list_all_of1_instance = ProductListAllOf1.from_json(json)
# print the JSON string representation of the object
print ProductListAllOf1.to_json()

# convert the object into a dict
product_list_all_of1_dict = product_list_all_of1_instance.to_dict()
# create an instance of ProductListAllOf1 from a dict
product_list_all_of1_form_dict = product_list_all_of1.from_dict(product_list_all_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


