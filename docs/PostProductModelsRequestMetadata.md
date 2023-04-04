# PostProductModelsRequestMetadata

More information around the product model (only available since the v2.3 in the Enterprise Edition)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_status** | **str** | Status of the product model regarding the user permissions | [optional] 

## Example

```python
from openapi_client.models.post_product_models_request_metadata import PostProductModelsRequestMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of PostProductModelsRequestMetadata from a JSON string
post_product_models_request_metadata_instance = PostProductModelsRequestMetadata.from_json(json)
# print the JSON string representation of the object
print PostProductModelsRequestMetadata.to_json()

# convert the object into a dict
post_product_models_request_metadata_dict = post_product_models_request_metadata_instance.to_dict()
# create an instance of PostProductModelsRequestMetadata from a dict
post_product_models_request_metadata_form_dict = post_product_models_request_metadata.from_dict(post_product_models_request_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


