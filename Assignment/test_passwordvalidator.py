import unittest
import passwordvalidator

class TestPasswordValidator(unittest.TestCase):

    def test_that_the_password_validator_function_exists(self):
        passwordvalidator.strong_password("semicolon")

    def test_that_the_password_is_strong(self):
        self.assertTrue(passwordvalidator.strong_password("semicolon1234"))


    def test_that_short_password_are_invalid(self):
        self.assertFalse(passwordvalidator.strong_password("pass"))
