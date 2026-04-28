import unittest
from unittest.mock import patch
import ex3

class TestTotal(unittest.TestCase):

    def test_calculate_total(self):
        with patch('ex3.read') as mock_read:
            mock_read.return_value = [10.5, 20.0, 4.5]
            result = ex3.calculate_total('orice_fisier.txt')

            self.assertEqual(result, 35.0)
            mock_read.assert_called_once_with('orice_fisier.txt')

if __name__ == '__main__':
    unittest.main()