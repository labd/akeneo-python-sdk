# ProductModelListAllOfMetadata

More information around the product model (only available since the v2.3 in the Enterprise Edition)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_status** | **str** | Status of the product model regarding the user permissions | [optional] 

## Example

```python
from openapi_client.models.product_model_list_all_of_metadata import ProductModelListAllOfMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ProductModelListAllOfMetadata from a JSON string
product_model_list_all_of_metadata_instance = ProductModelListAllOfMetadata.from_json(json)
# print the JSON string representation of the object
print ProductModelListAllOfMetadata.to_json()

# convert the object into a dict
product_model_list_all_of_metadata_dict = product_model_list_all_of_metadata_instance.to_dict()
# create an instance of ProductModelListAllOfMetadata from a dict
product_model_list_all_of_metadata_form_dict = product_model_list_all_of_metadata.from_dict(product_model_list_all_of_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


