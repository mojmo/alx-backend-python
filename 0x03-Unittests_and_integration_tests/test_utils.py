#!/usr/bin/env python3

"""This script defines unit tests for the `access_nested_map`, `get_json`,
and `memoize` functions.

The `access_nested_map` function retrieves a value from a nested map
(dictionary) based on a provided path (a sequence of keys).

The `get_json` function retrieves JSON data from a remote URL.

The `memoize` decorator caches the result of a function call.

This test suite uses parameterized tests to verify the functionality
of all functions.
"""

from parameterized import parameterized
import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test suite for the `access_nested_map` function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Tests retrieving a value from a nested map using a path.

        Args:
            nested_map: The nested map (dictionary) to access.
            path: A tuple of keys representing the path to the desired value.
            expected: The expected value retrieved from the nested map.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test that a KeyError is raised.

        Args:
            nested_map: The nested map (dictionary) to access.
            path: A tuple of keys representing the path to the desired value.
            expected: The expected value retrieved from the nested map.
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(repr(cm.exception), f"KeyError('{expected}')")


class TestGetJson(unittest.TestCase):
    """Test suite for the `get_json` function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Tests that `get_json` returns the expected JSON data.

        Args:
            test_url: The URL to fetch JSON data from (mocked).
            test_payload: The expected payload returned by the mocked response.
        """
        with patch("requests.get") as mock_get:
            mock_get.return_value.json.return_value = test_payload
            result = get_json(test_url)
            self.assertEqual(result, test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test suite for the `memoize` decorator."""

    def test_memoize(self):
        """Tests that the `memoize` decorator caches function calls."""

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_obj = TestClass()

        # Patch the a_method to verify it's called only once
        with patch.object(test_obj, "a_method") as mock_method:
            # Call the memoized property twice
            result1 = test_obj.a_property
            result2 = test_obj.a_property

            self.assertEqual(result1, result2)
            mock_method.assert_called_once_with()
