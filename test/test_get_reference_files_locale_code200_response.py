# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.get_reference_files_locale_code200_response import GetReferenceFilesLocaleCode200Response  # noqa: E501
from openapi_client.rest import ApiException

class TestGetReferenceFilesLocaleCode200Response(unittest.TestCase):
    """GetReferenceFilesLocaleCode200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetReferenceFilesLocaleCode200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetReferenceFilesLocaleCode200Response`
        """
        model = openapi_client.models.get_reference_files_locale_code200_response.GetReferenceFilesLocaleCode200Response()  # noqa: E501
        if include_optional :
            return GetReferenceFilesLocaleCode200Response(
                code = '', 
                locale = '', 
                link = openapi_client.models.get_reference_files__locale_code__200_response__link.get_reference_files__locale_code__200_response__link(
                    download = openapi_client.models.pam_assets__embedded_items_inner_all_of_reference_files_inner__link_download.PAM_Assets__embedded_items_inner_allOf_reference_files_inner__link_download(
                        href = '', ), )
            )
        else :
            return GetReferenceFilesLocaleCode200Response(
        )
        """

    def testGetReferenceFilesLocaleCode200Response(self):
        """Test GetReferenceFilesLocaleCode200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
