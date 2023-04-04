# ProductModelsEmbeddedItemsInnerAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Product model code | 
**family** | **str** | &lt;a href&#x3D;&#39;api-reference.html#Family&#39;&gt;Family&lt;/a&gt; code  from which the product inherits its attributes and attributes requirements (since the 3.2) | [optional] 
**family_variant** | **str** | Family variant code from which the product model inherits its attributes and variant attributes | 
**parent** | **str** | Code of the parent &lt;a href&#x3D;&#39;api-reference.html#Productmodel&#39;&gt;product model&lt;/a&gt;. This parent can be modified since the 2.3. | [optional] [default to 'null']
**categories** | **List[str]** | Codes of the &lt;a href&#x3D;&#39;api-reference.html#Category&#39;&gt;categories&lt;/a&gt; in which the product model is categorized | [optional] 
**values** | **Dict[str, List[ProductModelsEmbeddedItemsInnerAllOfValuesValueInner]]** | Product model attributes values, see &lt;a href&#x3D;&#39;/concepts/products.html#focus-on-the-product-values&#39;&gt;Product values&lt;/a&gt; section for more details | [optional] 
**associations** | [**ProductModelsEmbeddedItemsInnerAllOfAssociations**](ProductModelsEmbeddedItemsInnerAllOfAssociations.md) |  | [optional] 
**quantified_associations** | [**ProductModelsEmbeddedItemsInnerAllOfQuantifiedAssociations**](ProductModelsEmbeddedItemsInnerAllOfQuantifiedAssociations.md) |  | [optional] 
**created** | **str** | Date of creation | [optional] 
**updated** | **str** | Date of the last update | [optional] 
**metadata** | [**ProductModelsEmbeddedItemsInnerAllOfMetadata**](ProductModelsEmbeddedItemsInnerAllOfMetadata.md) |  | [optional] 
**quality_scores** | **object** | Product model quality scores for each channel/locale combination (&lt;strong&gt;only available since the 7.0 version&lt;/strong&gt; and when the \&quot;with_quality_scores\&quot; query parameter is set to \&quot;true\&quot;) | [optional] 

## Example

```python
from akeneo.models.product_models_embedded_items_inner_all_of import ProductModelsEmbeddedItemsInnerAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of ProductModelsEmbeddedItemsInnerAllOf from a JSON string
product_models_embedded_items_inner_all_of_instance = ProductModelsEmbeddedItemsInnerAllOf.from_json(json)
# print the JSON string representation of the object
print ProductModelsEmbeddedItemsInnerAllOf.to_json()

# convert the object into a dict
product_models_embedded_items_inner_all_of_dict = product_models_embedded_items_inner_all_of_instance.to_dict()
# create an instance of ProductModelsEmbeddedItemsInnerAllOf from a dict
product_models_embedded_items_inner_all_of_form_dict = product_models_embedded_items_inner_all_of.from_dict(product_models_embedded_items_inner_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


