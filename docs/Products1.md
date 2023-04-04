# Products1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**Products1Embedded**](Products1Embedded.md) |  | [optional] 
**links** | [**ProductsLinks**](ProductsLinks.md) |  | [optional] 
**current_page** | **int** | Current page number | [optional] 

## Example

```python
from openapi_client.models.products1 import Products1

# TODO update the JSON string below
json = "{}"
# create an instance of Products1 from a JSON string
products1_instance = Products1.from_json(json)
# print the JSON string representation of the object
print Products1.to_json()

# convert the object into a dict
products1_dict = products1_instance.to_dict()
# create an instance of Products1 from a dict
products1_form_dict = products1.from_dict(products1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


