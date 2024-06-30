#!/usr/bin/env python3

"""This script defines unit tests for the `GithubOrgClient.org` class."""

from parameterized import parameterized
import unittest
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for the `GithubOrgClient.org` class."""

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

    @patch('client.get_json')
    def test_public_repos_url(self, mock):
        """
        Tests that `GithubOrgClient.public_repos_url` returns the
        expected value.
        """

        # Mocked organization data
        mocked_org_data = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }

        mock.return_value = mocked_org_data

        # Create an instance of GithubOrgClient
        client = GithubOrgClient("google")

        # Get the public repos URL
        public_repos_url = client._public_repos_url

        # Assert the expected URL
        self.assertEqual(public_repos_url, mocked_org_data["repos_url"])
