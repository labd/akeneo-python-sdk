# PublishedProductListAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Published product identifier, i.e. the value of the only &#x60;pim_catalog_identifier&#x60; attribute | 
**enabled** | **bool** | Whether the published product is enable | [optional] [default to True]
**family** | **str** | &lt;a href&#x3D;&#39;api-reference.html#Family&#39;&gt;Family&lt;/a&gt; code from which the published product inherits its attributes and attributes requirements | [optional] [default to 'null']
**categories** | **List[str]** | Codes of the &lt;a href&#x3D;&#39;api-reference.html#Category&#39;&gt;categories&lt;/a&gt; in which the published product is classified | [optional] 
**groups** | **List[str]** | Codes of the groups to which the published product belong | [optional] 
**values** | **Dict[str, List[object]]** | Published product attributes values, see &lt;a href&#x3D;&#39;/concepts/products.html#focus-on-the-product-values&#39;&gt;Product values&lt;/a&gt; section for more details | [optional] 
**associations** | [**PublishedProductListAllOfAssociations**](PublishedProductListAllOfAssociations.md) |  | [optional] 
**quantified_associations** | **object** | Warning: associations with quantities are not compatible with the published products. The response will always be empty. | [optional] 
**created** | **str** | Date of creation | [optional] 
**updated** | **str** | Date of the last update | [optional] 

## Example

```python
from openapi_client.models.published_product_list_all_of import PublishedProductListAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of PublishedProductListAllOf from a JSON string
published_product_list_all_of_instance = PublishedProductListAllOf.from_json(json)
# print the JSON string representation of the object
print PublishedProductListAllOf.to_json()

# convert the object into a dict
published_product_list_all_of_dict = published_product_list_all_of_instance.to_dict()
# create an instance of PublishedProductListAllOf from a dict
published_product_list_all_of_form_dict = published_product_list_all_of.from_dict(published_product_list_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


