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
from openapi_client.models.get_products401_response import GetProducts401Response  # noqa: E501
from openapi_client.rest import ApiException

class TestGetProducts401Response(unittest.TestCase):
    """GetProducts401Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetProducts401Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetProducts401Response`
        """
        model = openapi_client.models.get_products401_response.GetProducts401Response()  # noqa: E501
        if include_optional :
            return GetProducts401Response(
                code = 56, 
                message = ''
            )
        else :
            return GetProducts401Response(
        )
        """

    def testGetProducts401Response(self):
        """Test GetProducts401Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
