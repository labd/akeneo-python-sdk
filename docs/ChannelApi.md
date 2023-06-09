# akeneo.ChannelApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**channels_patch**](ChannelApi.md#channels_patch) | **PATCH** /api/rest/v1/channels/{code} | Update/create a channel
[**channels_post**](ChannelApi.md#channels_post) | **POST** /api/rest/v1/channels | Create a new channel
[**get_channels**](ChannelApi.md#get_channels) | **GET** /api/rest/v1/channels | Get a list of channels
[**get_channels_code**](ChannelApi.md#get_channels_code) | **GET** /api/rest/v1/channels/{code} | Get a channel
[**several_channels_patch**](ChannelApi.md#several_channels_patch) | **PATCH** /api/rest/v1/channels | Update/create several channels


# **channels_patch**
> channels_patch(code, body)

Update/create a channel

This endpoint allows you to update a given channel. Know more about <a href=\"/documentation/update.html#update-behavior\">Update behavior</a>. Note that if no channel exists for the given code, it creates it.

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
    api_instance = akeneo.ChannelApi(api_client)
    code = 'code_example' # str | Code of the resource
    body = akeneo.ChannelsEmbeddedItemsInnerAllOf() # ChannelsEmbeddedItemsInnerAllOf | 

    try:
        # Update/create a channel
        api_instance.channels_patch(code, body)
    except Exception as e:
        print("Exception when calling ChannelApi->channels_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Code of the resource | 
 **body** | [**ChannelsEmbeddedItemsInnerAllOf**](ChannelsEmbeddedItemsInnerAllOf.md)|  | 

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
**201** | Created |  * Location - URI of the created resource <br>  |
**204** | No content to return |  * Location - URI of the created resource <br>  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**403** | Access forbidden |  -  |
**415** | Unsupported Media type |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channels_post**
> channels_post(body=body)

Create a new channel

This endpoint allows you to create a new channel.

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
    api_instance = akeneo.ChannelApi(api_client)
    body = akeneo.ChannelsEmbeddedItemsInnerAllOf() # ChannelsEmbeddedItemsInnerAllOf |  (optional)

    try:
        # Create a new channel
        api_instance.channels_post(body=body)
    except Exception as e:
        print("Exception when calling ChannelApi->channels_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChannelsEmbeddedItemsInnerAllOf**](ChannelsEmbeddedItemsInnerAllOf.md)|  | [optional] 

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
**201** | Created |  * Location - URI of the created resource <br>  |
**400** | Bad request |  -  |
**401** | Authentication required |  -  |
**403** | Access forbidden |  -  |
**415** | Unsupported Media type |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channels**
> Channels get_channels(page=page, limit=limit, with_count=with_count)

Get a list of channels

This endpoint allows you to get a list of channels. Channels are paginated and sorted by code.

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
    api_instance = akeneo.ChannelApi(api_client)
    page = 1 # int | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section (optional) (default to 1)
    limit = 10 # int | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section (optional) (default to 10)
    with_count = False # bool | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way (optional) (default to False)

    try:
        # Get a list of channels
        api_response = api_instance.get_channels(page=page, limit=limit, with_count=with_count)
        print("The response of ChannelApi->get_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelApi->get_channels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1]
 **limit** | **int**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10]
 **with_count** | **bool**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to False]

### Return type

[**Channels**](Channels.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, _links, current_page, _embedded, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return channels paginated |  -  |
**401** | Authentication required |  -  |
**403** | Access forbidden |  -  |
**406** | Not Acceptable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channels_code**
> ChannelsEmbeddedItemsInnerAllOf get_channels_code(code)

Get a channel

This endpoint allows you to get the information about a given channel.

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
    api_instance = akeneo.ChannelApi(api_client)
    code = 'code_example' # str | Code of the resource

    try:
        # Get a channel
        api_response = api_instance.get_channels_code(code)
        print("The response of ChannelApi->get_channels_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelApi->get_channels_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Code of the resource | 

### Return type

[**ChannelsEmbeddedItemsInnerAllOf**](ChannelsEmbeddedItemsInnerAllOf.md)

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
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**406** | Not Acceptable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **several_channels_patch**
> PatchProducts200Response several_channels_patch(body=body)

Update/create several channels

This endpoint allows you to update and/or create several channels at once.

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
    api_instance = akeneo.ChannelApi(api_client)
    body = akeneo.SeveralChannelsPatchRequest() # SeveralChannelsPatchRequest |  (optional)

    try:
        # Update/create several channels
        api_response = api_instance.several_channels_patch(body=body)
        print("The response of ChannelApi->several_channels_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelApi->several_channels_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SeveralChannelsPatchRequest**](SeveralChannelsPatchRequest.md)|  | [optional] 

### Return type

[**PatchProducts200Response**](PatchProducts200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, x-example-1, x-example-2, x-example-3, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication required |  -  |
**403** | Access forbidden |  -  |
**413** | Request Entity Too Large |  -  |
**415** | Unsupported Media type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

