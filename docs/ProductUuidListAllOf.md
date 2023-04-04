# ProductUuidListAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Product uuid | [optional] 
**enabled** | **bool** | Whether the product is enabled | [optional] [default to True]
**family** | **str** | &lt;a href&#x3D;&#39;api-reference.html#Family&#39;&gt;Family&lt;/a&gt; code from which the product inherits its attributes and attributes requirements. | [optional] [default to 'null only in the case of a non variant product']
**categories** | **List[str]** | Codes of the &lt;a href&#x3D;&#39;api-reference.html#Category&#39;&gt;categories&lt;/a&gt; in which the product is classified | [optional] 
**groups** | **List[str]** | Codes of the groups to which the product belong | [optional] 
**parent** | **str** | Code of the parent &lt;a href&#x3D;&#39;api-reference.html#Productmodel&#39;&gt;product model&lt;/a&gt; when the product is a variant (only available since the 2.0). This parent can be modified since the 2.3. | [optional] [default to 'null']
**values** | **Dict[str, List[object]]** | Product attributes values, see &lt;a href&#x3D;&#39;/concepts/products.html#focus-on-the-product-values&#39;&gt;Product values&lt;/a&gt; section for more details | [optional] 
**associations** | [**ProductUuidListAllOfAssociations**](ProductUuidListAllOfAssociations.md) |  | [optional] 
**quantified_associations** | [**ProductUuidListAllOfQuantifiedAssociations**](ProductUuidListAllOfQuantifiedAssociations.md) |  | [optional] 
**created** | **str** | Date of creation | [optional] 
**updated** | **str** | Date of the last update | [optional] 
**metadata** | [**ProductListAllOf1Metadata**](ProductListAllOf1Metadata.md) |  | [optional] 
**quality_scores** | **object** | Product quality scores for each channel/locale combination (only available since the 5.0 and when the \&quot;with_quality_scores\&quot; query parameter is set to \&quot;true\&quot;) | [optional] 
**completenesses** | [**List[ProductListAllOf1Completenesses]**](ProductListAllOf1Completenesses.md) | Product completenesses for each channel/locale combination (only available since the 7.0 version, and when the \&quot;with_completenesses\&quot; query parameter is set to \&quot;true\&quot;) | [optional] 

## Example

```python
from openapi_client.models.product_uuid_list_all_of import ProductUuidListAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of ProductUuidListAllOf from a JSON string
product_uuid_list_all_of_instance = ProductUuidListAllOf.from_json(json)
# print the JSON string representation of the object
print ProductUuidListAllOf.to_json()

# convert the object into a dict
product_uuid_list_all_of_dict = product_uuid_list_all_of_instance.to_dict()
# create an instance of ProductUuidListAllOf from a dict
product_uuid_list_all_of_form_dict = product_uuid_list_all_of.from_dict(product_uuid_list_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


