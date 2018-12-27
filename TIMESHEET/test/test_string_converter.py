from unittest import TestCase

from TIMESHEET.string_converter import string_converter


class TestString_converter(TestCase):
    converter = string_converter()

    def test_convert_to_int(self):
        result = self.converter.convert_to_int("12")
        self.assertEqual(result, 12)

    def test_convert_to_int_with_halves(self):
        result = self.converter.convert_to_int("12.5")
        self.assertEqual(result, 12.5)

    def test_erron_on_wrong_decimal(self):
        self.assertRaises(TypeError, self.converter.convert_to_int, "12.3")

    def test_convert_commas(self):
        result = self.converter.convert_to_int("12,5")
        self.assertEqual(result, 12.5)

    def test_not_a_number(self):
        result = self.converter.convert_to_int("12,5,")
        self.assertEqual(result,"This is not a correct entry")
