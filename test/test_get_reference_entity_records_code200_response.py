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
from openapi_client.models.get_reference_entity_records_code200_response import GetReferenceEntityRecordsCode200Response  # noqa: E501
from openapi_client.rest import ApiException

class TestGetReferenceEntityRecordsCode200Response(unittest.TestCase):
    """GetReferenceEntityRecordsCode200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetReferenceEntityRecordsCode200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetReferenceEntityRecordsCode200Response`
        """
        model = openapi_client.models.get_reference_entity_records_code200_response.GetReferenceEntityRecordsCode200Response()  # noqa: E501
        if include_optional :
            return GetReferenceEntityRecordsCode200Response(
                code = '', 
                values = openapi_client.models.patch_reference_entity_records_request_inner_values.patch_reference_entity_records_request_inner_values(
                    attribute_code = [
                        openapi_client.models.patch_reference_entity_records_request_inner_values_attribute_code_inner.patch_reference_entity_records_request_inner_values_attributeCode_inner(
                            channel = '', 
                            locale = '', 
                            data = openapi_client.models.data.data(), )
                        ], ), 
                created = 'null', 
                updated = 'null'
            )
        else :
            return GetReferenceEntityRecordsCode200Response(
                code = '',
        )
        """

    def testGetReferenceEntityRecordsCode200Response(self):
        """Test GetReferenceEntityRecordsCode200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
