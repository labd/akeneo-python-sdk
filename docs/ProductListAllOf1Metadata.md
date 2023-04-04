# ProductListAllOf1Metadata

More information around the product (only available since the v2.0 in the Enterprise Edition)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_status** | **str** | Status of the product regarding the user permissions | [optional] 

## Example

```python
from akeneo.models.product_list_all_of1_metadata import ProductListAllOf1Metadata

# TODO update the JSON string below
json = "{}"
# create an instance of ProductListAllOf1Metadata from a JSON string
product_list_all_of1_metadata_instance = ProductListAllOf1Metadata.from_json(json)
# print the JSON string representation of the object
print ProductListAllOf1Metadata.to_json()

# convert the object into a dict
product_list_all_of1_metadata_dict = product_list_all_of1_metadata_instance.to_dict()
# create an instance of ProductListAllOf1Metadata from a dict
product_list_all_of1_metadata_form_dict = product_list_all_of1_metadata.from_dict(product_list_all_of1_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


