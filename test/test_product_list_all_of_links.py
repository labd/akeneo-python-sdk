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
from openapi_client.models.product_list_all_of_links import ProductListAllOfLinks  # noqa: E501
from openapi_client.rest import ApiException

class TestProductListAllOfLinks(unittest.TestCase):
    """ProductListAllOfLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProductListAllOfLinks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductListAllOfLinks`
        """
        model = openapi_client.models.product_list_all_of_links.ProductListAllOfLinks()  # noqa: E501
        if include_optional :
            return ProductListAllOfLinks(
                var_self = openapi_client.models.product_list_all_of__links_self.ProductList_allOf__links_self(
                    href = '', )
            )
        else :
            return ProductListAllOfLinks(
        )
        """

    def testProductListAllOfLinks(self):
        """Test ProductListAllOfLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
