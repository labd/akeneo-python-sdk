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
from openapi_client.api.channel_api import ChannelApi  # noqa: E501
from openapi_client.rest import ApiException


class TestChannelApi(unittest.TestCase):
    """ChannelApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.channel_api.ChannelApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_channels_patch(self):
        """Test case for channels_patch

        Update/create a channel  # noqa: E501
        """
        pass

    def test_channels_post(self):
        """Test case for channels_post

        Create a new channel  # noqa: E501
        """
        pass

    def test_get_channels(self):
        """Test case for get_channels

        Get a list of channels  # noqa: E501
        """
        pass

    def test_get_channels_code(self):
        """Test case for get_channels_code

        Get a channel  # noqa: E501
        """
        pass

    def test_several_channels_patch(self):
        """Test case for several_channels_patch

        Update/create several channels  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
