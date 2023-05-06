from unittest import TestCase, main
from task_32.convert_an_array_into_a_2D_array_with_conditions import Solution


class FindMatrixTest(TestCase):
    solution = Solution()

    def test_one_positive(self):
        self.assertEqual(self.solution.findMatrix(nums=[1, 3, 4, 1, 2, 3, 1]),
                         [[1, 3, 4, 2], [1, 3], [1]])


    def test_two_positive(self):

        self.assertEqual(self.solution.findMatrix(nums=[1, 2, 3, 4]),
                         [[1, 2, 3, 4]])


    def test_negative(self):
        self.assertNotEqual(self.solution.findMatrix(nums=[5, 2, 2, 7, 5, 2, 6, 1]),
                            [[5, 2, 7, 6, 1], [2], [2, 5]])



if __name__ == '__main__':
    main()