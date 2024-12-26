"""Test module for the application."""

import unittest
import transform

class TestStringMethods(unittest.TestCase):
    """Test case for string transformation methods."""

    def test_to_upper(self):
        """Test case for the to_upper_case function."""
        string = transform.to_upper_case("hello")
        self.assertEqual(string, "HELLO")

    def test_to_lower(self):
        """Test case for the to_lower_case function."""
        string = transform.to_lower_case("HELLO")
        self.assertEqual(string, "hello")

    def test_to_capitalize(self):
        """Test case for the to_capitalize function."""
        string = transform.to_capitalize("HELLO")
        self.assertEqual(string, "Hello")

if __name__ == '__main__':
    unittest.main()
