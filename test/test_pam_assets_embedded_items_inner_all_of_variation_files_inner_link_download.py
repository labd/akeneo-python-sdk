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
from openapi_client.models.pam_assets_embedded_items_inner_all_of_variation_files_inner_link_download import PAMAssetsEmbeddedItemsInnerAllOfVariationFilesInnerLinkDownload  # noqa: E501
from openapi_client.rest import ApiException

class TestPAMAssetsEmbeddedItemsInnerAllOfVariationFilesInnerLinkDownload(unittest.TestCase):
    """PAMAssetsEmbeddedItemsInnerAllOfVariationFilesInnerLinkDownload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PAMAssetsEmbeddedItemsInnerAllOfVariationFilesInnerLinkDownload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PAMAssetsEmbeddedItemsInnerAllOfVariationFilesInnerLinkDownload`
        """
        model = openapi_client.models.pam_assets_embedded_items_inner_all_of_variation_files_inner_link_download.PAMAssetsEmbeddedItemsInnerAllOfVariationFilesInnerLinkDownload()  # noqa: E501
        if include_optional :
            return PAMAssetsEmbeddedItemsInnerAllOfVariationFilesInnerLinkDownload(
                href = ''
            )
        else :
            return PAMAssetsEmbeddedItemsInnerAllOfVariationFilesInnerLinkDownload(
        )
        """

    def testPAMAssetsEmbeddedItemsInnerAllOfVariationFilesInnerLinkDownload(self):
        """Test PAMAssetsEmbeddedItemsInnerAllOfVariationFilesInnerLinkDownload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
