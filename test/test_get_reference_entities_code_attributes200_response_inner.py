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
from openapi_client.models.get_reference_entities_code_attributes200_response_inner import GetReferenceEntitiesCodeAttributes200ResponseInner  # noqa: E501
from openapi_client.rest import ApiException

class TestGetReferenceEntitiesCodeAttributes200ResponseInner(unittest.TestCase):
    """GetReferenceEntitiesCodeAttributes200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetReferenceEntitiesCodeAttributes200ResponseInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetReferenceEntitiesCodeAttributes200ResponseInner`
        """
        model = openapi_client.models.get_reference_entities_code_attributes200_response_inner.GetReferenceEntitiesCodeAttributes200ResponseInner()  # noqa: E501
        if include_optional :
            return GetReferenceEntitiesCodeAttributes200ResponseInner(
                code = '', 
                labels = openapi_client.models.attributes__embedded_items_inner_all_of_labels.Attributes__embedded_items_inner_allOf_labels(
                    locale_code = '', ), 
                type = 'text', 
                value_per_locale = True, 
                value_per_channel = True, 
                is_required_for_completeness = True, 
                max_characters = 56, 
                is_textarea = True, 
                is_rich_text_editor = True, 
                validation_rule = 'none', 
                validation_regexp = '', 
                allowed_extensions = [
                    ''
                    ], 
                max_file_size = '', 
                reference_entity_code = '', 
                decimals_allowed = True, 
                min_value = '', 
                max_value = ''
            )
        else :
            return GetReferenceEntitiesCodeAttributes200ResponseInner(
                code = '',
                type = 'text',
        )
        """

    def testGetReferenceEntitiesCodeAttributes200ResponseInner(self):
        """Test GetReferenceEntitiesCodeAttributes200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
