from unittest import TestCase, main
from task_39.sum_of_absolute_differences_in_a_sorted_array import Solution


class SumAbsoluteDifferencesTest(TestCase):
    solution = Solution()

    def test_one_positive(self):
        self.assertEqual(self.solution.getSumAbsoluteDifferences(nums=[2, 3, 5]),
                         [4, 3, 5])


    def test_two_positive(self):
        self.assertEqual(self.solution.getSumAbsoluteDifferences(nums=[1, 4, 6, 8, 10]),
                         [24, 15, 13, 15, 21])


    def test_negative(self):
        self.assertNotEqual(self.solution.getSumAbsoluteDifferences(nums=[1, 3, 5, 7, 9, 15]),
                            [35, 26, 22, 22, 26, 50])


if __name__ == '__main__':
    main()
