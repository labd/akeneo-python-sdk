# akeneo.ReferenceEntityMediaFileApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_reference_entity_media_files_code**](ReferenceEntityMediaFileApi.md#get_reference_entity_media_files_code) | **GET** /api/rest/v1/reference-entities-media-files/{code} | Download the media file associated to a reference entity or a record
[**post_reference_entity_media_files**](ReferenceEntityMediaFileApi.md#post_reference_entity_media_files) | **POST** /api/rest/v1/reference-entities-media-files | Create a new media file for a reference entity or a record


# **get_reference_entity_media_files_code**
> get_reference_entity_media_files_code(code)

Download the media file associated to a reference entity or a record

This endpoint allows you to download a given media file that is associated with a reference entity or a record.

### Example

```python
from __future__ import print_function
import time
import os
import akeneo
from akeneo.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://demo.akeneo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = akeneo.Configuration(
    host = "http://demo.akeneo.com"
)


# Enter a context with an instance of the API client
with akeneo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = akeneo.ReferenceEntityMediaFileApi(api_client)
    code = 'code_example' # str | Code of the resource

    try:
        # Download the media file associated to a reference entity or a record
        api_instance.get_reference_entity_media_files_code(code)
    except Exception as e:
        print("Exception when calling ReferenceEntityMediaFileApi->get_reference_entity_media_files_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Code of the resource | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication required |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_reference_entity_media_files**
> post_reference_entity_media_files(content_type, body=body)

Create a new media file for a reference entity or a record

This endpoint allows you to create a new media file and associate it to the image of a reference entity, or to the main image or to an attribute value of a record.

### Example

```python
from __future__ import print_function
import time
import os
import akeneo
from akeneo.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://demo.akeneo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = akeneo.Configuration(
    host = "http://demo.akeneo.com"
)


# Enter a context with an instance of the API client
with akeneo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = akeneo.ReferenceEntityMediaFileApi(api_client)
    content_type = 'content_type_example' # str | Equal to 'multipart/form-data', no other value allowed
    body = akeneo.PostReferenceEntityMediaFilesRequest() # PostReferenceEntityMediaFilesRequest |  (optional)

    try:
        # Create a new media file for a reference entity or a record
        api_instance.post_reference_entity_media_files(content_type, body=body)
    except Exception as e:
        print("Exception when calling ReferenceEntityMediaFileApi->post_reference_entity_media_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Equal to &#39;multipart/form-data&#39;, no other value allowed | 
 **body** | [**PostReferenceEntityMediaFilesRequest**](PostReferenceEntityMediaFilesRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message, _links

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Reference-entities-media-file-code - Code of the media file <br>  * Location - URI of the created resource <br>  |
**401** | Authentication required |  -  |
**415** | Unsupported Media type |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

