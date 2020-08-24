"""Test cases for command line
"""

from unittest import TestCase

from userpass.command_line import main


class TestCmd(TestCase):
    """Test Case Class
    """
    def test_basic(self):
        """test main function returns without error
        """
        main()
