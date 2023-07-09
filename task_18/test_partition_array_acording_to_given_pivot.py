from unittest import TestCase, main
from task_18.partition_array_acording_to_given_pivot import Solution


class CountDigitsTest(TestCase):
    solution = Solution()

    def test_one_positive(self):
        self.assertEqual(self.solution.pivotArray(nums=[9, 12, 5, 10, 14, 3, 10], pivot=10),
                         [9, 5, 3, 10, 10, 12, 14])


    def test_two_positive(self):
        self.assertEqual(self.solution.pivotArray(nums=[-3, 4, 3, 2], pivot=2), [-3, 2, 4, 3])


    def test_negative(self):
        self.assertNotEqual(self.solution.pivotArray(nums=[1, -1, -5, 0], pivot=1), [-5, 0, 1, -1])



if __name__ == '__main__':
    main()