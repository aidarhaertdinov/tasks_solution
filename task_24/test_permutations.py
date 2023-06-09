from unittest import TestCase, main
from task_24.permutations import Solution


class PermutationsTest(TestCase):
    solution = Solution()

    def test_one_positive(self):
        self.assertEqual(self.solution.permute(nums=[1, 2, 3]),
                         [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])


    def test_two_positive(self):
        self.assertEqual(self.solution.permute(nums=[0, 1]), [[0, 1], [1, 0]])


    def test_three_positive(self):
        self.assertEqual(self.solution.permute(nums=[1]), [[1]])


    def test_negative(self):
        self.assertNotEqual(self.solution.permute(nums=[1, 2]), [[2, 1]])



if __name__ == '__main__':
    main()