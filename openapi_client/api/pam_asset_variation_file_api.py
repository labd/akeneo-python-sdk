# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictStr

from typing import Optional

from openapi_client.models.get_variation_files_channel_code_locale_code200_response import GetVariationFilesChannelCodeLocaleCode200Response
from openapi_client.models.post_reference_files_locale_code_request import PostReferenceFilesLocaleCodeRequest

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class PAMAssetVariationFileApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_variation_files_channel_code_locale_code(self, asset_code : Annotated[StrictStr, Field(..., description="Code of the asset")], channel_code : Annotated[StrictStr, Field(..., description="Code of the channel")], locale_code : Annotated[StrictStr, Field(..., description="Code of the locale if the asset is localizable or equal to `no-locale` if the asset is not localizable")], **kwargs) -> GetVariationFilesChannelCodeLocaleCode200Response:  # noqa: E501
        """Get a variation file  # noqa: E501

        This endpoint allows you to get the information about a variation file of a given PAM asset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_variation_files_channel_code_locale_code(asset_code, channel_code, locale_code, async_req=True)
        >>> result = thread.get()

        :param asset_code: Code of the asset (required)
        :type asset_code: str
        :param channel_code: Code of the channel (required)
        :type channel_code: str
        :param locale_code: Code of the locale if the asset is localizable or equal to `no-locale` if the asset is not localizable (required)
        :type locale_code: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetVariationFilesChannelCodeLocaleCode200Response
        """
        kwargs['_return_http_data_only'] = True
        return self.get_variation_files_channel_code_locale_code_with_http_info(asset_code, channel_code, locale_code, **kwargs)  # noqa: E501

    @validate_arguments
    def get_variation_files_channel_code_locale_code_with_http_info(self, asset_code : Annotated[StrictStr, Field(..., description="Code of the asset")], channel_code : Annotated[StrictStr, Field(..., description="Code of the channel")], locale_code : Annotated[StrictStr, Field(..., description="Code of the locale if the asset is localizable or equal to `no-locale` if the asset is not localizable")], **kwargs):  # noqa: E501
        """Get a variation file  # noqa: E501

        This endpoint allows you to get the information about a variation file of a given PAM asset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_variation_files_channel_code_locale_code_with_http_info(asset_code, channel_code, locale_code, async_req=True)
        >>> result = thread.get()

        :param asset_code: Code of the asset (required)
        :type asset_code: str
        :param channel_code: Code of the channel (required)
        :type channel_code: str
        :param locale_code: Code of the locale if the asset is localizable or equal to `no-locale` if the asset is not localizable (required)
        :type locale_code: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetVariationFilesChannelCodeLocaleCode200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'asset_code',
            'channel_code',
            'locale_code'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_variation_files_channel_code_locale_code" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['asset_code']:
            _path_params['asset_code'] = _params['asset_code']
        if _params['channel_code']:
            _path_params['channel_code'] = _params['channel_code']
        if _params['locale_code']:
            _path_params['locale_code'] = _params['locale_code']

        # process the query parameters
        _query_params = []

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'code', 'message'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "GetVariationFilesChannelCodeLocaleCode200Response",
            '401': "GetProducts401Response",
            '403': "GetProducts401Response",
            '404': "GetProducts401Response",
            '406': "GetProducts401Response",
        }

        return self.api_client.call_api(
            '/api/rest/v1/assets/{asset_code}/variation-files/{channel_code}/{locale_code}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_variation_files_channel_code_locale_code_download(self, asset_code : Annotated[StrictStr, Field(..., description="Code of the asset")], channel_code : Annotated[StrictStr, Field(..., description="Code of the channel")], locale_code : Annotated[StrictStr, Field(..., description="Code of the locale if the asset is localizable or equal to `no-locale` if the asset is not localizable")], **kwargs) -> None:  # noqa: E501
        """Download a variation file  # noqa: E501

        This endpoint allows you to download a given variation file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_variation_files_channel_code_locale_code_download(asset_code, channel_code, locale_code, async_req=True)
        >>> result = thread.get()

        :param asset_code: Code of the asset (required)
        :type asset_code: str
        :param channel_code: Code of the channel (required)
        :type channel_code: str
        :param locale_code: Code of the locale if the asset is localizable or equal to `no-locale` if the asset is not localizable (required)
        :type locale_code: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.get_variation_files_channel_code_locale_code_download_with_http_info(asset_code, channel_code, locale_code, **kwargs)  # noqa: E501

    @validate_arguments
    def get_variation_files_channel_code_locale_code_download_with_http_info(self, asset_code : Annotated[StrictStr, Field(..., description="Code of the asset")], channel_code : Annotated[StrictStr, Field(..., description="Code of the channel")], locale_code : Annotated[StrictStr, Field(..., description="Code of the locale if the asset is localizable or equal to `no-locale` if the asset is not localizable")], **kwargs):  # noqa: E501
        """Download a variation file  # noqa: E501

        This endpoint allows you to download a given variation file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_variation_files_channel_code_locale_code_download_with_http_info(asset_code, channel_code, locale_code, async_req=True)
        >>> result = thread.get()

        :param asset_code: Code of the asset (required)
        :type asset_code: str
        :param channel_code: Code of the channel (required)
        :type channel_code: str
        :param locale_code: Code of the locale if the asset is localizable or equal to `no-locale` if the asset is not localizable (required)
        :type locale_code: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'asset_code',
            'channel_code',
            'locale_code'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_variation_files_channel_code_locale_code_download" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['asset_code']:
            _path_params['asset_code'] = _params['asset_code']
        if _params['channel_code']:
            _path_params['channel_code'] = _params['channel_code']
        if _params['locale_code']:
            _path_params['locale_code'] = _params['locale_code']

        # process the query parameters
        _query_params = []

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'code', 'message'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/api/rest/v1/assets/{asset_code}/variation-files/{channel_code}/{locale_code}/download', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def post_variation_files_channel_code_locale_code(self, asset_code : Annotated[StrictStr, Field(..., description="Code of the asset")], channel_code : Annotated[StrictStr, Field(..., description="Code of the channel")], locale_code : Annotated[StrictStr, Field(..., description="Code of the locale if the asset is localizable or equal to `no-locale` if the asset is not localizable")], content_type : Annotated[StrictStr, Field(..., description="Equal to 'multipart/form-data', no other value allowed")], body : Optional[PostReferenceFilesLocaleCodeRequest] = None, **kwargs) -> None:  # noqa: E501
        """Upload a new variation file  # noqa: E501

        This endpoint allows you to upload a new variation file for a given PAM asset, channel and locale.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.post_variation_files_channel_code_locale_code(asset_code, channel_code, locale_code, content_type, body, async_req=True)
        >>> result = thread.get()

        :param asset_code: Code of the asset (required)
        :type asset_code: str
        :param channel_code: Code of the channel (required)
        :type channel_code: str
        :param locale_code: Code of the locale if the asset is localizable or equal to `no-locale` if the asset is not localizable (required)
        :type locale_code: str
        :param content_type: Equal to 'multipart/form-data', no other value allowed (required)
        :type content_type: str
        :param body:
        :type body: PostReferenceFilesLocaleCodeRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.post_variation_files_channel_code_locale_code_with_http_info(asset_code, channel_code, locale_code, content_type, body, **kwargs)  # noqa: E501

    @validate_arguments
    def post_variation_files_channel_code_locale_code_with_http_info(self, asset_code : Annotated[StrictStr, Field(..., description="Code of the asset")], channel_code : Annotated[StrictStr, Field(..., description="Code of the channel")], locale_code : Annotated[StrictStr, Field(..., description="Code of the locale if the asset is localizable or equal to `no-locale` if the asset is not localizable")], content_type : Annotated[StrictStr, Field(..., description="Equal to 'multipart/form-data', no other value allowed")], body : Optional[PostReferenceFilesLocaleCodeRequest] = None, **kwargs):  # noqa: E501
        """Upload a new variation file  # noqa: E501

        This endpoint allows you to upload a new variation file for a given PAM asset, channel and locale.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.post_variation_files_channel_code_locale_code_with_http_info(asset_code, channel_code, locale_code, content_type, body, async_req=True)
        >>> result = thread.get()

        :param asset_code: Code of the asset (required)
        :type asset_code: str
        :param channel_code: Code of the channel (required)
        :type channel_code: str
        :param locale_code: Code of the locale if the asset is localizable or equal to `no-locale` if the asset is not localizable (required)
        :type locale_code: str
        :param content_type: Equal to 'multipart/form-data', no other value allowed (required)
        :type content_type: str
        :param body:
        :type body: PostReferenceFilesLocaleCodeRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'asset_code',
            'channel_code',
            'locale_code',
            'content_type',
            'body'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_variation_files_channel_code_locale_code" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['asset_code']:
            _path_params['asset_code'] = _params['asset_code']
        if _params['channel_code']:
            _path_params['channel_code'] = _params['channel_code']
        if _params['locale_code']:
            _path_params['locale_code'] = _params['locale_code']

        # process the query parameters
        _query_params = []

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['content_type']:
            _header_params['Content-Type'] = _params['content_type']

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None
        if _params['body']:
            _body_params = _params['body']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'code', 'message', '_links'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/api/rest/v1/assets/{asset_code}/variation-files/{channel_code}/{locale_code}', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
