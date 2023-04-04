# ProductsLinks


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**ProductsLinksSelf**](ProductsLinksSelf.md) |  | [optional] 
**first** | [**ProductsLinksFirst**](ProductsLinksFirst.md) |  | [optional] 
**previous** | [**ProductsLinksPrevious**](ProductsLinksPrevious.md) |  | [optional] 
**next** | [**ProductsLinksNext**](ProductsLinksNext.md) |  | [optional] 

## Example

```python
from akeneo.models.products_links import ProductsLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ProductsLinks from a JSON string
products_links_instance = ProductsLinks.from_json(json)
# print the JSON string representation of the object
print ProductsLinks.to_json()

# convert the object into a dict
products_links_dict = products_links_instance.to_dict()
# create an instance of ProductsLinks from a dict
products_links_form_dict = products_links.from_dict(products_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


