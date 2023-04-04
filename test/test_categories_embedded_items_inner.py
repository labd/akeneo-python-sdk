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
from openapi_client.models.categories_embedded_items_inner import CategoriesEmbeddedItemsInner  # noqa: E501
from openapi_client.rest import ApiException

class TestCategoriesEmbeddedItemsInner(unittest.TestCase):
    """CategoriesEmbeddedItemsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CategoriesEmbeddedItemsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CategoriesEmbeddedItemsInner`
        """
        model = openapi_client.models.categories_embedded_items_inner.CategoriesEmbeddedItemsInner()  # noqa: E501
        if include_optional :
            return CategoriesEmbeddedItemsInner(
                links = openapi_client.models.products__embedded_items_inner_all_of__links.Products__embedded_items_inner_allOf__links(
                    self = openapi_client.models.products__embedded_items_inner_all_of__links_self.Products__embedded_items_inner_allOf__links_self(
                        href = '', ), ), 
                code = '', 
                parent = '', 
                updated = '', 
                position = 56, 
                labels = openapi_client.models.categories__embedded_items_inner_all_of_labels.Categories__embedded_items_inner_allOf_labels(
                    locale_code = '', ), 
                values = openapi_client.models.categories__embedded_items_inner_all_of_values.Categories__embedded_items_inner_allOf_values(
                    additional_properties|attribute_uuid|channel_code|locale_code = [
                        openapi_client.models.categories__embedded_items_inner_all_of_values_additional_properties_attribute_uuid_channel_code_locale_code_inner.Categories__embedded_items_inner_allOf_values_additionalProperties_attributeUuid_channelCode_localeCode_inner(
                            data = openapi_client.models.data.data(), 
                            type = '', 
                            locale = '', 
                            channel = '', 
                            attribute_code = '', )
                        ], )
            )
        else :
            return CategoriesEmbeddedItemsInner(
                code = '',
        )
        """

    def testCategoriesEmbeddedItemsInner(self):
        """Test CategoriesEmbeddedItemsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
