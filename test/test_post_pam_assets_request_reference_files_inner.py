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
from openapi_client.models.post_pam_assets_request_reference_files_inner import PostPamAssetsRequestReferenceFilesInner  # noqa: E501
from openapi_client.rest import ApiException

class TestPostPamAssetsRequestReferenceFilesInner(unittest.TestCase):
    """PostPamAssetsRequestReferenceFilesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PostPamAssetsRequestReferenceFilesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostPamAssetsRequestReferenceFilesInner`
        """
        model = openapi_client.models.post_pam_assets_request_reference_files_inner.PostPamAssetsRequestReferenceFilesInner()  # noqa: E501
        if include_optional :
            return PostPamAssetsRequestReferenceFilesInner(
                link = openapi_client.models.post_pam_assets_request_reference_files_inner__link.post_pam_assets_request_reference_files_inner__link(
                    self = openapi_client.models.post_pam_assets_request_reference_files_inner__link_self.post_pam_assets_request_reference_files_inner__link_self(
                        href = '', ), 
                    download = openapi_client.models.post_pam_assets_request_reference_files_inner__link_download.post_pam_assets_request_reference_files_inner__link_download(
                        href = '', ), ), 
                locale = '', 
                code = ''
            )
        else :
            return PostPamAssetsRequestReferenceFilesInner(
        )
        """

    def testPostPamAssetsRequestReferenceFilesInner(self):
        """Test PostPamAssetsRequestReferenceFilesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
