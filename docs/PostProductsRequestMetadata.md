# PostProductsRequestMetadata

More information around the product (only available since the v2.0 in the Enterprise Edition)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_status** | **str** | Status of the product regarding the user permissions | [optional] 

## Example

```python
from akeneo.models.post_products_request_metadata import PostProductsRequestMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of PostProductsRequestMetadata from a JSON string
post_products_request_metadata_instance = PostProductsRequestMetadata.from_json(json)
# print the JSON string representation of the object
print PostProductsRequestMetadata.to_json()

# convert the object into a dict
post_products_request_metadata_dict = post_products_request_metadata_instance.to_dict()
# create an instance of PostProductsRequestMetadata from a dict
post_products_request_metadata_form_dict = post_products_request_metadata.from_dict(post_products_request_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


