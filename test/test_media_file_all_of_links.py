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
from openapi_client.models.media_file_all_of_links import MediaFileAllOfLinks  # noqa: E501
from openapi_client.rest import ApiException

class TestMediaFileAllOfLinks(unittest.TestCase):
    """MediaFileAllOfLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MediaFileAllOfLinks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MediaFileAllOfLinks`
        """
        model = openapi_client.models.media_file_all_of_links.MediaFileAllOfLinks()  # noqa: E501
        if include_optional :
            return MediaFileAllOfLinks(
                download = openapi_client.models.media_file_all_of__links_download.MediaFile_allOf__links_download(
                    href = '', )
            )
        else :
            return MediaFileAllOfLinks(
        )
        """

    def testMediaFileAllOfLinks(self):
        """Test MediaFileAllOfLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
