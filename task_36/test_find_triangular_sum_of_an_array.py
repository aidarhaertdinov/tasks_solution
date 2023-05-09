from unittest import TestCase, main
from task_36.find_triangular_sum_of_an_array import Solution


class TriangularSumTest(TestCase):
    solution = Solution()

    def test_one_positive(self):
        self.assertEqual(self.solution.triangularSum(nums=[1, 2, 3, 4, 5]), 8)

    def test_two_positive(self):
        self.assertEqual(self.solution.triangularSum(nums=[2, 3, 4, 5, 6]), 4)

    def test_negative(self):
        self.assertNotEqual(self.solution.triangularSum(nums=[1, 2, 3, 4, 5, 6, 7, 8]), 5)


if __name__ == '__main__':
    main()
