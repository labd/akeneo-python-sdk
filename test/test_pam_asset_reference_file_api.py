# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.pam_asset_reference_file_api import PAMAssetReferenceFileApi  # noqa: E501
from openapi_client.rest import ApiException


class TestPAMAssetReferenceFileApi(unittest.TestCase):
    """PAMAssetReferenceFileApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.pam_asset_reference_file_api.PAMAssetReferenceFileApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_reference_files_channel_code_locale_code_download(self):
        """Test case for get_reference_files_channel_code_locale_code_download

        Download a reference file  # noqa: E501
        """
        pass

    def test_get_reference_files_locale_code(self):
        """Test case for get_reference_files_locale_code

        Get a reference file  # noqa: E501
        """
        pass

    def test_post_reference_files_locale_code(self):
        """Test case for post_reference_files_locale_code

        Upload a new reference file  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
