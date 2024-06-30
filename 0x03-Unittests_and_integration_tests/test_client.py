#!/usr/bin/env python3

"""This script defines unit tests for the `GithubOrgClient.org` method."""

from parameterized import parameterized
import unittest
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for the `GithubOrgClient.org` method."""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org, mock):
        """Tests that `GithubOrgClient.org` returns the expected value.

        Args:
            org: The name of the organization to fetch information for.
        """
        client = GithubOrgClient(org)

        client.org()

        mock.assert_called_once_with(
            f"https://api.github.com/orgs/{org}"
        )
