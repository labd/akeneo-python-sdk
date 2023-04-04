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
from openapi_client.models.reference_entity_item_list import ReferenceEntityItemList  # noqa: E501
from openapi_client.rest import ApiException

class TestReferenceEntityItemList(unittest.TestCase):
    """ReferenceEntityItemList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ReferenceEntityItemList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReferenceEntityItemList`
        """
        model = openapi_client.models.reference_entity_item_list.ReferenceEntityItemList()  # noqa: E501
        if include_optional :
            return ReferenceEntityItemList(
                links = openapi_client.models.reference_entities__embedded_items_inner_all_of__links.Reference_Entities__embedded_items_inner_allOf__links(
                    self = openapi_client.models.products__embedded_items_inner_all_of__links_self.Products__embedded_items_inner_allOf__links_self(
                        href = '', ), 
                    image_download = openapi_client.models.reference_entities__embedded_items_inner_all_of__links_image_download.Reference_Entities__embedded_items_inner_allOf__links_image_download(
                        href = '', ), )
            )
        else :
            return ReferenceEntityItemList(
        )
        """

    def testReferenceEntityItemList(self):
        """Test ReferenceEntityItemList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
