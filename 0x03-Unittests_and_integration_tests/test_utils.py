#!/usr/bin/env python3

"""This script defines unit tests for the `access_nested_map` function.
This test suite uses parameterized tests to verify the functionality of
`access_nested_map` with various nested dictionaries and paths.
"""

from parameterized import parameterized
import unittest
from utils import access_nested_map


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
