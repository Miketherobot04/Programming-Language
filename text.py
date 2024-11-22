
import unittest
from functions import calculate_sum, string_length, update_dictionary

class TestFunctions(unittest.TestCase):
    # Tests for calculate_sum
    def test_sum_positive_numbers(self):
        self.assertEqual(calculate_sum(5, 10), 15)

    def test_sum_negative_numbers(self):
        self.assertEqual(calculate_sum(-5, -10), -15)

    def test_sum_mixed_numbers(self):
        self.assertEqual(calculate_sum(5, -10), -5)

    # Tests for string_length
    def test_string_length(self):
        self.assertEqual(string_length("hello"), 5)

    def test_empty_string(self):
        self.assertEqual(string_length(""), 0)

    # Tests for update_dictionary
    def test_key_exists(self):
        my_dict = {'a': 1}
        update_dictionary(my_dict, 'a', 10)
        self.assertEqual(my_dict['a'], 11)

    def test_key_does_not_exist(self):
        my_dict = {}
        update_dictionary(my_dict, 'b', 20)
        self.assertEqual(my_dict['b'], 20)

if __name__ == "__main__":
    unittest.main()
