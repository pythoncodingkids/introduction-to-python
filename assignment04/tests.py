import unittest
import solution04


class TestAssignment4(unittest.TestCase):

    def test_minutes_in_between(self):
        self.assertEqual(0, solution04.minutes_in_between(2, 30, 2, 30))
        self.assertEqual(10, solution04.minutes_in_between(2, 30, 2, 40))
        self.assertEqual(70, solution04.minutes_in_between(2, 30, 3, 40))
        self.assertEqual(70, solution04.minutes_in_between(23, 30, 0, 40))
        self.assertEqual(130, solution04.minutes_in_between(23, 30, 1, 40))
        self.assertEqual(1310, solution04.minutes_in_between(1, 40, 23, 30))

    def test_fibonacci(self):
        self.assertEqual([0], solution04.fibonacci(1))
        self.assertEqual([0, 1], solution04.fibonacci(2))
        self.assertEqual([0, 1, 1, 2, 3, 5, 8, 13, 21, 34], solution04.fibonacci(10))

    def test_find_max_min_difference(self):
        self.assertEqual(0, solution04.find_max_min_difference([0]))
        self.assertEqual(4, solution04.find_max_min_difference([1, 2, 3, 4, 5]))
        self.assertEqual(0, solution04.find_max_min_difference([3, 3, 3, 3, 3]))
        self.assertEqual(2, solution04.find_max_min_difference([5, 3, 5, 3, 3]))

    def test_less_than(self):
        self.assertEqual([], solution04.less_than([1, 2, 3], 1))
        self.assertEqual([1], solution04.less_than([1, 2, 3], 2))
        self.assertEqual([2, 2], solution04.less_than([2, 2, 3], 3))

    def test_reverse_list(self):
        self.assertEqual([], solution04.reverse_list([]))
        self.assertEqual([1], solution04.reverse_list([1]))
        self.assertEqual([2, 1], solution04.reverse_list([1, 2]))
        self.assertEqual([2, 1, 3], solution04.reverse_list([3, 1, 2]))

    def test_shift_list_by_1(self):
        self.assertEqual([1], solution04.shift_list_by_1([1]))
        self.assertEqual([3, 1, 2], solution04.shift_list_by_1([1, 2, 3]))

    def test_shift_list_by_n(self):
        self.assertEqual([1], solution04.shift_list([1], 5))
        self.assertEqual([5, 6, 1, 2, 3, 4], solution04.shift_list([1, 2, 3, 4, 5, 6], 2))

    def test_nth_odd_number(self):
        self.assertEqual(None, solution04.nth_odd_number([1], 2))
        self.assertEqual(3, solution04.nth_odd_number([1, 2, 3, 4, 5], 2))

    def test_line_values(self):
        self.assertEqual([2, 4, 6, 8], solution04.line_values(2, 2, 0, 3))
        self.assertEqual([-4, -2, 0, 2, 4, 6, 8], solution04.line_values(2, 2, -3, 3))

    def test_non_duplicates(self):
        self.assertEqual([], solution04.non_duplicates([2, 2]))
        self.assertEqual([3, 5, 9], solution04.non_duplicates([2, 2, 3, 4, 5, 4, 7, 9, 7]))