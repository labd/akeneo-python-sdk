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
from openapi_client.models.post_pam_assets_request_variation_files_inner_link import PostPamAssetsRequestVariationFilesInnerLink  # noqa: E501
from openapi_client.rest import ApiException

class TestPostPamAssetsRequestVariationFilesInnerLink(unittest.TestCase):
    """PostPamAssetsRequestVariationFilesInnerLink unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PostPamAssetsRequestVariationFilesInnerLink
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostPamAssetsRequestVariationFilesInnerLink`
        """
        model = openapi_client.models.post_pam_assets_request_variation_files_inner_link.PostPamAssetsRequestVariationFilesInnerLink()  # noqa: E501
        if include_optional :
            return PostPamAssetsRequestVariationFilesInnerLink(
                var_self = openapi_client.models.post_pam_assets_request_variation_files_inner__link_self.post_pam_assets_request_variation_files_inner__link_self(
                    href = '', ), 
                download = openapi_client.models.post_pam_assets_request_variation_files_inner__link_download.post_pam_assets_request_variation_files_inner__link_download(
                    href = '', )
            )
        else :
            return PostPamAssetsRequestVariationFilesInnerLink(
        )
        """

    def testPostPamAssetsRequestVariationFilesInnerLink(self):
        """Test PostPamAssetsRequestVariationFilesInnerLink"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
