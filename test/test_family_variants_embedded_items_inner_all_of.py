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
from openapi_client.models.family_variants_embedded_items_inner_all_of import FamilyVariantsEmbeddedItemsInnerAllOf  # noqa: E501
from openapi_client.rest import ApiException

class TestFamilyVariantsEmbeddedItemsInnerAllOf(unittest.TestCase):
    """FamilyVariantsEmbeddedItemsInnerAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FamilyVariantsEmbeddedItemsInnerAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FamilyVariantsEmbeddedItemsInnerAllOf`
        """
        model = openapi_client.models.family_variants_embedded_items_inner_all_of.FamilyVariantsEmbeddedItemsInnerAllOf()  # noqa: E501
        if include_optional :
            return FamilyVariantsEmbeddedItemsInnerAllOf(
                code = '', 
                variant_attribute_sets = [
                    openapi_client.models.family_variants__embedded_items_inner_all_of_variant_attribute_sets_inner.Family_Variants__embedded_items_inner_allOf_variant_attribute_sets_inner(
                        level = 56, 
                        axes = [
                            ''
                            ], 
                        attributes = [
                            ''
                            ], )
                    ], 
                labels = openapi_client.models.family_variants__embedded_items_inner_all_of_labels.Family_Variants__embedded_items_inner_allOf_labels(
                    locale_code = '', )
            )
        else :
            return FamilyVariantsEmbeddedItemsInnerAllOf(
                code = '',
                variant_attribute_sets = [
                    openapi_client.models.family_variants__embedded_items_inner_all_of_variant_attribute_sets_inner.Family_Variants__embedded_items_inner_allOf_variant_attribute_sets_inner(
                        level = 56, 
                        axes = [
                            ''
                            ], 
                        attributes = [
                            ''
                            ], )
                    ],
        )
        """

    def testFamilyVariantsEmbeddedItemsInnerAllOf(self):
        """Test FamilyVariantsEmbeddedItemsInnerAllOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
