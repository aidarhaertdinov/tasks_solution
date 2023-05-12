from unittest import TestCase, main
from task_41.minimum_time_to_make_rope_colorful import Solution


class MinCostTest(TestCase):
    solution = Solution()

    def test_one_positive(self):
        self.assertEqual(self.solution.minCost(colors="abaac", neededTime=[1, 2, 3, 4, 5]), 3)


    def test_two_positive(self):
        self.assertEqual(self.solution.minCost(colors="abc", neededTime=[1, 2, 3]), 0)


    def test_three_positive(self):
        self.assertEqual(self.solution.minCost(colors="aabaa", neededTime=[1, 2, 3, 4, 1]), 2)


    def test_negative(self):
        self.assertNotEqual(self.solution.minCost(colors="aabbbaccc", neededTime=[1, 2, 3, 4, 5, 6, 7, 8, 9]), 22)


if __name__ == '__main__':
    main()
