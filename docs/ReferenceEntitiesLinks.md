# ReferenceEntitiesLinks


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**ProductsLinksSelf**](ProductsLinksSelf.md) |  | [optional] 
**first** | [**ProductsLinksFirst**](ProductsLinksFirst.md) |  | [optional] 
**next** | [**ProductsLinksNext**](ProductsLinksNext.md) |  | [optional] 

## Example

```python
from akeneo.models.reference_entities_links import ReferenceEntitiesLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceEntitiesLinks from a JSON string
reference_entities_links_instance = ReferenceEntitiesLinks.from_json(json)
# print the JSON string representation of the object
print ReferenceEntitiesLinks.to_json()

# convert the object into a dict
reference_entities_links_dict = reference_entities_links_instance.to_dict()
# create an instance of ReferenceEntitiesLinks from a dict
reference_entities_links_form_dict = reference_entities_links.from_dict(reference_entities_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


