# Attributes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**AttributesEmbedded**](AttributesEmbedded.md) |  | [optional] 
**links** | [**ProductsLinks**](ProductsLinks.md) |  | [optional] 
**current_page** | **int** | Current page number | [optional] 

## Example

```python
from openapi_client.models.attributes import Attributes

# TODO update the JSON string below
json = "{}"
# create an instance of Attributes from a JSON string
attributes_instance = Attributes.from_json(json)
# print the JSON string representation of the object
print Attributes.to_json()

# convert the object into a dict
attributes_dict = attributes_instance.to_dict()
# create an instance of Attributes from a dict
attributes_form_dict = attributes.from_dict(attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


