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
from openapi_client.models.reference_entity_record_embedded import ReferenceEntityRecordEmbedded  # noqa: E501
from openapi_client.rest import ApiException

class TestReferenceEntityRecordEmbedded(unittest.TestCase):
    """ReferenceEntityRecordEmbedded unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ReferenceEntityRecordEmbedded
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReferenceEntityRecordEmbedded`
        """
        model = openapi_client.models.reference_entity_record_embedded.ReferenceEntityRecordEmbedded()  # noqa: E501
        if include_optional :
            return ReferenceEntityRecordEmbedded(
                items = [
                    openapi_client.models.reference_entity_record__embedded_items_inner.Reference_entity_record__embedded_items_inner()
                    ]
            )
        else :
            return ReferenceEntityRecordEmbedded(
        )
        """

    def testReferenceEntityRecordEmbedded(self):
        """Test ReferenceEntityRecordEmbedded"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
