import unittest
import transform


class TestStringMethods(unittest.TestCase):

    def test_to_upper(self):
        sting = transform.to_upper_case("hello")
        self.assertEqual(sting, "HELLO")

    def test_to_lower(self):
        sting = transform.to_lower_case("HELLO")
        self.assertEqual(sting, "hello")

    def test_to_capitalize(self):
        sting = transform.to_capitalize("HELLO")
        self.assertEqual(sting, "Hello")


if __name__ == '__main__':
    unittest.main()
