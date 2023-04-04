# ErrorByLine


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line** | **int** | Line number | [optional] 
**identifier** | **str** | Resource identifier, only filled when the resource is a product | [optional] 
**code** | **str** | Resource code, only filled when the resource is not a product | [optional] 
**status_code** | **int** | HTTP status code, see &lt;a href&#x3D;\&quot;/documentation/responses.html#client-errors\&quot;&gt;Client errors&lt;/a&gt; to understand the meaning of each code | [optional] 
**message** | **str** | Message explaining the error | [optional] 

## Example

```python
from akeneo.models.error_by_line import ErrorByLine

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorByLine from a JSON string
error_by_line_instance = ErrorByLine.from_json(json)
# print the JSON string representation of the object
print ErrorByLine.to_json()

# convert the object into a dict
error_by_line_dict = error_by_line_instance.to_dict()
# create an instance of ErrorByLine from a dict
error_by_line_form_dict = error_by_line.from_dict(error_by_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


