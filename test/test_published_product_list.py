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
from openapi_client.models.published_product_list import PublishedProductList  # noqa: E501
from openapi_client.rest import ApiException

class TestPublishedProductList(unittest.TestCase):
    """PublishedProductList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PublishedProductList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PublishedProductList`
        """
        model = openapi_client.models.published_product_list.PublishedProductList()  # noqa: E501
        if include_optional :
            return PublishedProductList(
                links = openapi_client.models.product_list_all_of__links.ProductList_allOf__links(
                    self = openapi_client.models.product_list_all_of__links_self.ProductList_allOf__links_self(
                        href = '', ), ), 
                identifier = '', 
                enabled = True, 
                family = '', 
                categories = [
                    ''
                    ], 
                groups = [
                    ''
                    ], 
                values = {
                    'key' : [
                        None
                        ]
                    }, 
                associations = openapi_client.models.published_product_list_all_of_associations.PublishedProductList_allOf_associations(
                    association_type_code = openapi_client.models.published_product_list_all_of_associations_association_type_code.PublishedProductList_allOf_associations_associationTypeCode(
                        groups = [
                            ''
                            ], 
                        products = [
                            ''
                            ], 
                        product_models = [
                            ''
                            ], ), ), 
                quantified_associations = None, 
                created = '', 
                updated = ''
            )
        else :
            return PublishedProductList(
                identifier = '',
        )
        """

    def testPublishedProductList(self):
        """Test PublishedProductList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
