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
from openapi_client.models.products import Products  # noqa: E501
from openapi_client.rest import ApiException

class TestProducts(unittest.TestCase):
    """Products unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Products
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Products`
        """
        model = openapi_client.models.products.Products()  # noqa: E501
        if include_optional :
            return Products(
                embedded = openapi_client.models.products__embedded.Products__embedded(
                    items = [
                        openapi_client.models.products__embedded_items_inner.Products__embedded_items_inner()
                        ], ), 
                links = openapi_client.models.products__links.Products__links(
                    self = openapi_client.models.products__links_self.Products__links_self(
                        href = '', ), 
                    first = openapi_client.models.products__links_first.Products__links_first(
                        href = '', ), 
                    previous = openapi_client.models.products__links_previous.Products__links_previous(
                        href = '', ), 
                    next = openapi_client.models.products__links_next.Products__links_next(
                        href = '', ), ), 
                current_page = 56
            )
        else :
            return Products(
        )
        """

    def testProducts(self):
        """Test Products"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
