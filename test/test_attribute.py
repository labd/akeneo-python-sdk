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
from openapi_client.models.attribute import Attribute  # noqa: E501
from openapi_client.rest import ApiException

class TestAttribute(unittest.TestCase):
    """Attribute unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Attribute
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Attribute`
        """
        model = openapi_client.models.attribute.Attribute()  # noqa: E501
        if include_optional :
            return Attribute(
                code = '', 
                type = 'pim_catalog_identifier', 
                labels = openapi_client.models.attributes__embedded_items_inner_all_of_labels.Attributes__embedded_items_inner_allOf_labels(
                    locale_code = '', ), 
                group = '', 
                group_labels = openapi_client.models.attributes__embedded_items_inner_all_of_group_labels.Attributes__embedded_items_inner_allOf_group_labels(
                    locale_code = '', ), 
                sort_order = 56, 
                localizable = True, 
                scopable = True, 
                available_locales = [
                    ''
                    ], 
                unique = True, 
                useable_as_grid_filter = True, 
                max_characters = 56, 
                validation_rule = '', 
                validation_regexp = '', 
                wysiwyg_enabled = True, 
                number_min = '', 
                number_max = '', 
                decimals_allowed = True, 
                negative_allowed = True, 
                metric_family = '', 
                default_metric_unit = '', 
                date_min = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                date_max = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                allowed_extensions = [
                    ''
                    ], 
                max_file_size = '', 
                reference_data_name = '', 
                default_value = True, 
                table_configuration = [
                    openapi_client.models.attributes__embedded_items_inner_all_of_table_configuration_inner.Attributes__embedded_items_inner_allOf_table_configuration_inner(
                        code = '', 
                        data_type = 'select', 
                        validations = openapi_client.models.attributes__embedded_items_inner_all_of_table_configuration_inner_validations.Attributes__embedded_items_inner_allOf_table_configuration_inner_validations(
                            min = 1.337, 
                            max = 1.337, 
                            decimals_allowed = True, 
                            max_length = 1.337, ), 
                        labels = openapi_client.models.attributes__embedded_items_inner_all_of_table_configuration_inner_labels.Attributes__embedded_items_inner_allOf_table_configuration_inner_labels(
                            locale_code = '', ), 
                        is_required_for_completeness = True, )
                    ]
            )
        else :
            return Attribute(
                code = '',
                type = 'pim_catalog_identifier',
                group = '',
        )
        """

    def testAttribute(self):
        """Test Attribute"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
