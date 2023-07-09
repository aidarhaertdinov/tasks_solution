from unittest import TestCase, main
from task_15.split_a_string_in_balanced_strings import Solution


class BalancedStringsTest(TestCase):
    solution = Solution()

    def test_one_positive(self):
        self.assertEqual(self.solution.balancedStringSplit("RLRRLLRLRL"), 4)

    def test_two_positive(self):
        self.assertEqual(self.solution.balancedStringSplit("RLRRRLLRLL"), 2)

    def test_three_positive(self):
        self.assertEqual(self.solution.balancedStringSplit("LLLLRRRR"), 1)


    def test_negative(self):
        self.assertNotEqual(self.solution.balancedStringSplit("RLLLLLRRRR"), 3)


if __name__ == '__main__':
    main()