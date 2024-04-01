import unittest
import datetime
import date_checker

current_year = datetime.datetime.now().year


class TestDate(unittest.TestCase):
    def test_date1(self):
        with self.assertRaises(TypeError):
            date_checker.date_checker("text")

    def test_date2(self):
        result = date_checker.date_checker("15.03.2001")
        self.assertEqual(result, True, "Pass")

    def test_date3(self):
        with self.assertRaises(Exception):
            date_checker.date_checker("15.03.1956")

    def test_date4(self):
        with self.assertRaises(Exception):
            date_checker.date_checker(f"15.03.{current_year + 1}")
