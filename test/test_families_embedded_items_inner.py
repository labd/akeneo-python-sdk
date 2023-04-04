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
from openapi_client.models.families_embedded_items_inner import FamiliesEmbeddedItemsInner  # noqa: E501
from openapi_client.rest import ApiException

class TestFamiliesEmbeddedItemsInner(unittest.TestCase):
    """FamiliesEmbeddedItemsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FamiliesEmbeddedItemsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FamiliesEmbeddedItemsInner`
        """
        model = openapi_client.models.families_embedded_items_inner.FamiliesEmbeddedItemsInner()  # noqa: E501
        if include_optional :
            return FamiliesEmbeddedItemsInner(
                links = openapi_client.models.products__embedded_items_inner_all_of__links.Products__embedded_items_inner_allOf__links(
                    self = openapi_client.models.products__embedded_items_inner_all_of__links_self.Products__embedded_items_inner_allOf__links_self(
                        href = '', ), ), 
                code = '', 
                attribute_as_label = '', 
                attribute_as_image = '', 
                attributes = [
                    ''
                    ], 
                attribute_requirements = openapi_client.models.families__embedded_items_inner_all_of_attribute_requirements.Families__embedded_items_inner_allOf_attribute_requirements(
                    channel_code = [
                        ''
                        ], ), 
                labels = openapi_client.models.families__embedded_items_inner_all_of_labels.Families__embedded_items_inner_allOf_labels(
                    locale_code = '', )
            )
        else :
            return FamiliesEmbeddedItemsInner(
                code = '',
                attribute_as_label = '',
        )
        """

    def testFamiliesEmbeddedItemsInner(self):
        """Test FamiliesEmbeddedItemsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
