import unittest
from datetime import datetime as real_datetime
from unittest.mock import patch, Mock
import ex1


class TestLeapYear(unittest.TestCase):

    # Varianta 1: folosind patch decorator
    @patch('ex1.datetime.datetime')
    def test_is_leap_year_true_with_patch(self, mock_datetime):
        mock_datetime.today.return_value = real_datetime(2024, 1, 1)
        self.assertTrue(ex1.is_leap_year())

    @patch('ex1.datetime.datetime')
    def test_is_leap_year_false_with_patch(self, mock_datetime):
        mock_datetime.today.return_value = real_datetime(2023, 1, 1)
        self.assertFalse(ex1.is_leap_year())

    # Varianta 2: folosind Mock manual
    def test_is_leap_year_true_with_manual_mock(self):
        original_datetime = ex1.datetime.datetime
        try:
            fake_datetime = Mock()
            fake_datetime.today.return_value = real_datetime(2000, 1, 1)
            ex1.datetime.datetime = fake_datetime
            self.assertTrue(ex1.is_leap_year())
        finally:
            ex1.datetime.datetime = original_datetime

    def test_is_leap_year_false_with_manual_mock(self):
        original_datetime = ex1.datetime.datetime
        try:
            fake_datetime = Mock()
            fake_datetime.today.return_value = real_datetime(1900, 1, 1)
            ex1.datetime.datetime = fake_datetime
            self.assertFalse(ex1.is_leap_year())
        finally:
            ex1.datetime.datetime = original_datetime


if __name__ == '__main__':
    unittest.main()