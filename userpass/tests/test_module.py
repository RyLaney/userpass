"""Test cases for module
"""
from unittest import TestCase

import userpass.generate

class TestModule(TestCase):
    """Test Case class for module
    """
    def test_alphanumeric_is_string(self):
        """generate.alphanumeric should return a string
        """
        item = userpass.generate.alphanumeric(64)
        self.assertIsInstance(item, str)

    def test_alphanumeric_string_length_is_12(self):
        """generate.alphanumeric(12) should be 12 chars long
        """
        item = userpass.generate.alphanumeric(12)
        self.assertEqual(len(item), 12)

    def test_alphanumeric_string_length_is_64(self):
        """generate.alphanumeric(64) should be 64 chars long
        """
        item = userpass.generate.alphanumeric(64)
        self.assertEqual(len(item), 64)


    def test_passphrase_is_string(self):
        """generate.passphrase should return a string
        """
        item = userpass.generate.passphrase(4)
        self.assertIsInstance(item, str)

    def test_passphrase_number_of_words_is_4(self):
        """generate.passphrase(4) should have 4 words
        """
        item = userpass.generate.passphrase(4)
        self.assertEqual(len(item.split()), 4)

    def test_passphrase_number_of_words_is_8(self):
        """generate.passphrase(8) should have 8 words
        """
        item = userpass.generate.passphrase(8)
        self.assertEqual(len(item.split()), 8)



    def test_urlsafe_is_string_with_arg(self):
        """generate.token_urlsafe should return a string
        """
        item = userpass.generate.token_urlsafe(64)
        self.assertIsInstance(item, str)

    def test_urlsafe_works_without_arg(self):
        """generate.token_urlsafe should return a string
        """
        item = userpass.generate.token_urlsafe()
        self.assertIsInstance(item, str)


