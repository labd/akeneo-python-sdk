# AttributeOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**AttributeOptionsEmbedded**](AttributeOptionsEmbedded.md) |  | [optional] 
**links** | [**ProductsLinks**](ProductsLinks.md) |  | [optional] 
**current_page** | **int** | Current page number | [optional] 

## Example

```python
from akeneo.models.attribute_options import AttributeOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeOptions from a JSON string
attribute_options_instance = AttributeOptions.from_json(json)
# print the JSON string representation of the object
print AttributeOptions.to_json()

# convert the object into a dict
attribute_options_dict = attribute_options_instance.to_dict()
# create an instance of AttributeOptions from a dict
attribute_options_form_dict = attribute_options.from_dict(attribute_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


