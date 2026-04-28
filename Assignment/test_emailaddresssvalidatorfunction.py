import unittest
import emailaddresssvalidatorfunction

class EmailValidatorFunction(unittest.TestCase):

    def test_that_email_address_validator_function_exists(self):
        emailaddresssvalidatorfunction.email_validation("semicolon@")


    def test_that_email_address_is_valid(self):
        self.assertTrue(emailaddresssvalidatorfunction.email_validation("semicolon@gmail"))

    def test_that_email_address_is_invalid_if_it_ends_with_at(self):
        self.assertFalse(emailaddresssvalidatorfunction.email_validation("semicolon@"))

    def test_that_email_address_is_invalid_if_it_starts_with_at(self):
        self.assertFalse(emailaddresssvalidatorfunction.email_validation("@semicolon10"))

    def test_that_email_address_is_invalid_if_at_is_missing(self):
        self.assertFalse(emailaddresssvalidatorfunction.email_validation("semicolon"))


    def test_that_email_is_invalid_if_it_is_too_short(self):
        self.assertFalse(emailaddresssvalidatorfunction.email_validation("semi@16"))
