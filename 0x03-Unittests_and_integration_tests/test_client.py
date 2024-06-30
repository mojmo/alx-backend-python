#!/usr/bin/env python3

"""This script defines unit tests for the `GithubOrgClient.org` class."""

from parameterized import parameterized
import unittest
from unittest.mock import patch, PropertyMock
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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Tests that `GithubOrgClient.public_repos` returns the expected
        value.
        """
        mocked_org_data = {
            "repos_url": "https://api.github.com/orgs/google/repos",
        }

        # Mocked public repos payload
        mocked_repos_payload = [
            {"name": "repo1", "license": {"key": "MIT"}},
            {"name": "repo2", "license": {"key": "Apache-2.0"}},
            {"name": "repo3", "license": None},
        ]

        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:

            mock_org.return_value = mocked_org_data
            mock_get_json.return_value = mocked_repos_payload

            client = GithubOrgClient("google")

            # Get the list of public repos (no license filter)
            public_repos = client.public_repos()

            # Assert the expected list of repos
            self.assertEqual(public_repos, ["repo1", "repo2", "repo3"])

            # Assert that the mocked methods were called once
            mock_org.assert_called_once_with()
            mock_get_json.assert_called_once_with(mocked_org_data["repos_url"])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """
        Tests that `GithubOrgClient.has_license` returns the expected
        value.
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected_result)
