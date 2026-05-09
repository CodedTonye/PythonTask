import unittest
import dollarstonairaconversionfunction

class TestCurrencyConversionFunction(unittest.TestCase):

    def test_that_dollars_to_naira_function_exists(self):
        dollarstonairaconversionfunction.dollars_to_naira(10)
    
    def test_that_whole_number_conversions(self):
        self.assertEqual(dollarstonairaconversionfunction.dollars_to_naira(10),15500.0)


    def test_that_decimal_input(self):
        self.assertEqual(dollarstonairaconversionfunction.dollars_to_naira(14.65),22707.5)



