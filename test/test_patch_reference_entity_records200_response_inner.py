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
from openapi_client.models.patch_reference_entity_records200_response_inner import PatchReferenceEntityRecords200ResponseInner  # noqa: E501
from openapi_client.rest import ApiException

class TestPatchReferenceEntityRecords200ResponseInner(unittest.TestCase):
    """PatchReferenceEntityRecords200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PatchReferenceEntityRecords200ResponseInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchReferenceEntityRecords200ResponseInner`
        """
        model = openapi_client.models.patch_reference_entity_records200_response_inner.PatchReferenceEntityRecords200ResponseInner()  # noqa: E501
        if include_optional :
            return PatchReferenceEntityRecords200ResponseInner(
                code = '', 
                status_code = 56, 
                message = ''
            )
        else :
            return PatchReferenceEntityRecords200ResponseInner(
        )
        """

    def testPatchReferenceEntityRecords200ResponseInner(self):
        """Test PatchReferenceEntityRecords200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
