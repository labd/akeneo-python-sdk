# coding: utf-8

"""
    Akeneo PIM REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.locale_api import LocaleApi  # noqa: E501
from openapi_client.rest import ApiException


class TestLocaleApi(unittest.TestCase):
    """LocaleApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.locale_api.LocaleApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_locales(self):
        """Test case for get_locales

        Get a list of locales  # noqa: E501
        """
        pass

    def test_get_locales_code(self):
        """Test case for get_locales_code

        Get a locale  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
