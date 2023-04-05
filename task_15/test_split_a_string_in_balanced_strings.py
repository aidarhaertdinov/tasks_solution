from unittest import TestCase, main
from task_15.split_a_string_in_balanced_strings import Solution


class BalancedStringsTest(TestCase):

    def test_one_positive(self):
        self.assertEqual(Solution.balancedStringSplit(self, "RLRRLLRLRL"), 4)

    def test_two_positive(self):
        self.assertEqual(Solution.balancedStringSplit(self, "RLRRRLLRLL"), 2)

    def test_three_positive(self):
        self.assertEqual(Solution.balancedStringSplit(self, "LLLLRRRR"), 1)


    def test_negative(self):
        self.assertNotEqual(Solution.balancedStringSplit(self, "RLLLLLRRRR"), 3)


if __name__ == '__main__':
    main()