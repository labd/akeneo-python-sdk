# PostProductModelsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Product model code | 
**family** | **str** | &lt;a href&#x3D;&#39;api-reference.html#Family&#39;&gt;Family&lt;/a&gt; code  from which the product inherits its attributes and attributes requirements (since the 3.2) | [optional] 
**family_variant** | **str** | Family variant code from which the product model inherits its attributes and variant attributes | 
**parent** | **str** | Code of the parent &lt;a href&#x3D;&#39;api-reference.html#Productmodel&#39;&gt;product model&lt;/a&gt;. This parent can be modified since the 2.3. | [optional] [default to 'null']
**categories** | **List[str]** | Codes of the &lt;a href&#x3D;&#39;api-reference.html#Category&#39;&gt;categories&lt;/a&gt; in which the product model is categorized | [optional] 
**values** | [**PostProductModelsRequestValues**](PostProductModelsRequestValues.md) |  | [optional] 
**associations** | [**PostProductModelsRequestAssociations**](PostProductModelsRequestAssociations.md) |  | [optional] 
**quantified_associations** | [**PostProductModelsRequestQuantifiedAssociations**](PostProductModelsRequestQuantifiedAssociations.md) |  | [optional] 
**created** | **str** | Date of creation | [optional] 
**updated** | **str** | Date of the last update | [optional] 
**metadata** | [**PostProductModelsRequestMetadata**](PostProductModelsRequestMetadata.md) |  | [optional] 
**quality_scores** | **object** | Product model quality scores for each channel/locale combination (&lt;strong&gt;only available since the 7.0 version&lt;/strong&gt; and when the \&quot;with_quality_scores\&quot; query parameter is set to \&quot;true\&quot;) | [optional] 

## Example

```python
from openapi_client.models.post_product_models_request import PostProductModelsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostProductModelsRequest from a JSON string
post_product_models_request_instance = PostProductModelsRequest.from_json(json)
# print the JSON string representation of the object
print PostProductModelsRequest.to_json()

# convert the object into a dict
post_product_models_request_dict = post_product_models_request_instance.to_dict()
# create an instance of PostProductModelsRequest from a dict
post_product_models_request_form_dict = post_product_models_request.from_dict(post_product_models_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


