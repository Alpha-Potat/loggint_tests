import unittest
from unittest.mock import patch

from logging_testing.main import sum, sub, mult, div, main
import logging_testing.main


class test_valid_count(unittest.TestCase):

    @patch('logging_testing.main.time.sleep')
    def test_valid_count_sum(self, _):

        self.assertEqual(sum(5, 6),11)
        self.assertEqual(sum(6, 6),12)
        self.assertEqual(sum(7, 6),13)
        self.assertEqual(sum(10, 6),16)


    def test_valid_count_sub(self):
        mock_author="Net, ya avtor!"
        self.assertEqual(sub(5, 6),-1)
        self.assertEqual(sub(6, 6),0)
        self.assertEqual(sub(7, 6),1)
        self.assertEqual(sub(10, 6),4)


    def test_valid_count_mult(self):

        self.assertEqual(mult(5, 6),30)
        self.assertEqual(mult(6, 6),36)
        self.assertEqual(mult(7, 6),42)
        self.assertEqual(mult(10, 6),60)


    def test_valid_count_div(self):

        self.assertEqual(div(12, 6),2)
        self.assertEqual(div(6, 6),1)
        self.assertEqual(div(36, 6),6)
        self.assertEqual(div(42, 6),7)


    def test_valid_exc_0(self):

        self.assertRaises(ValueError, div, 5, 0)
        self.assertRaises(ValueError, div, 8, 0)
        self.assertRaises(ValueError, div, 0, 0)

    @patch('logging_testing.main.time.sleep')
    def test_valid_exc_values(self, _):

        self.assertRaises(TypeError, sum, [1,5], {'seven':'7'})
        self.assertRaises(TypeError, sub, 'seven', 0)
        self.assertRaises(TypeError, mult, (7,6), 0)
        self.assertRaises(TypeError, div, True, None)
    
    @patch.object(logging_testing.main, 'sum')
    def test_program_work(self, mock_sum):
        mock_sum.return_value=5
        self.assertRaises(ValueError, main)
        mock_sum.assert_called_once()
