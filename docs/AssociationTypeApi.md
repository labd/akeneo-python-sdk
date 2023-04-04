# akeneo.AssociationTypeApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**association_types_get**](AssociationTypeApi.md#association_types_get) | **GET** /api/rest/v1/association-types/{code} | Get an association type
[**association_types_get_list**](AssociationTypeApi.md#association_types_get_list) | **GET** /api/rest/v1/association-types | Get a list of association types
[**association_types_patch**](AssociationTypeApi.md#association_types_patch) | **PATCH** /api/rest/v1/association-types/{code} | Update/create an association type
[**association_types_post**](AssociationTypeApi.md#association_types_post) | **POST** /api/rest/v1/association-types | Create a new association type
[**several_association_types_patch**](AssociationTypeApi.md#several_association_types_patch) | **PATCH** /api/rest/v1/association-types | Update/create several association types


# **association_types_get**
> AssociationTypesEmbeddedItemsInnerAllOf association_types_get(code)

Get an association type

This endpoint allows you to get the information about a given association type.

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
    api_instance = akeneo.AssociationTypeApi(api_client)
    code = 'code_example' # str | Code of the resource

    try:
        # Get an association type
        api_response = api_instance.association_types_get(code)
        print("The response of AssociationTypeApi->association_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociationTypeApi->association_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Code of the resource | 

### Return type

[**AssociationTypesEmbeddedItemsInnerAllOf**](AssociationTypesEmbeddedItemsInnerAllOf.md)

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

# **association_types_get_list**
> AssociationTypes association_types_get_list(page=page, limit=limit, with_count=with_count)

Get a list of association types

This endpoint allows you to get a list of association types. Association types are paginated and sorted by code.

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
    api_instance = akeneo.AssociationTypeApi(api_client)
    page = 1 # int | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section (optional) (default to 1)
    limit = 10 # int | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section (optional) (default to 10)
    with_count = False # bool | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way (optional) (default to False)

    try:
        # Get a list of association types
        api_response = api_instance.association_types_get_list(page=page, limit=limit, with_count=with_count)
        print("The response of AssociationTypeApi->association_types_get_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociationTypeApi->association_types_get_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1]
 **limit** | **int**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10]
 **with_count** | **bool**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to False]

### Return type

[**AssociationTypes**](AssociationTypes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, _links, current_page, _embedded, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return association types paginated |  -  |
**401** | Authentication required |  -  |
**403** | Access forbidden |  -  |
**406** | Not Acceptable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **association_types_patch**
> association_types_patch(code, body)

Update/create an association type

This endpoint allows you to update a given association type. Know more about <a href=\"/documentation/update.html#update-behavior\">Update behavior</a>. Note that if no association type exists for the given code, it creates it.

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
    api_instance = akeneo.AssociationTypeApi(api_client)
    code = 'code_example' # str | Code of the resource
    body = akeneo.AssociationTypesEmbeddedItemsInnerAllOf() # AssociationTypesEmbeddedItemsInnerAllOf | 

    try:
        # Update/create an association type
        api_instance.association_types_patch(code, body)
    except Exception as e:
        print("Exception when calling AssociationTypeApi->association_types_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Code of the resource | 
 **body** | [**AssociationTypesEmbeddedItemsInnerAllOf**](AssociationTypesEmbeddedItemsInnerAllOf.md)|  | 

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

# **association_types_post**
> association_types_post(body=body)

Create a new association type

This endpoint allows you to create a new association type.

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
    api_instance = akeneo.AssociationTypeApi(api_client)
    body = akeneo.AssociationTypesEmbeddedItemsInnerAllOf() # AssociationTypesEmbeddedItemsInnerAllOf |  (optional)

    try:
        # Create a new association type
        api_instance.association_types_post(body=body)
    except Exception as e:
        print("Exception when calling AssociationTypeApi->association_types_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssociationTypesEmbeddedItemsInnerAllOf**](AssociationTypesEmbeddedItemsInnerAllOf.md)|  | [optional] 

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

# **several_association_types_patch**
> PatchProducts200Response several_association_types_patch(body=body)

Update/create several association types

This endpoint allows you to update and/or create several association types at once.

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
    api_instance = akeneo.AssociationTypeApi(api_client)
    body = akeneo.SeveralAssociationTypesPatchRequest() # SeveralAssociationTypesPatchRequest |  (optional)

    try:
        # Update/create several association types
        api_response = api_instance.several_association_types_patch(body=body)
        print("The response of AssociationTypeApi->several_association_types_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociationTypeApi->several_association_types_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SeveralAssociationTypesPatchRequest**](SeveralAssociationTypesPatchRequest.md)|  | [optional] 

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

