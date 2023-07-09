from unittest import TestCase, main
from task_5.build_array_from_permutation import Solution


class BuildArrayPermutationTest(TestCase):
    solution = Solution()

    def test_one_positive(self):
        self.assertEqual(self.solution.buildArray([0, 2, 1, 5, 3, 4]), [0, 1, 2, 4, 5, 3])

    def test_two_positive(self):
        self.assertEqual(self.solution.buildArray([5, 0, 1, 2, 3, 4]), [4, 5, 0, 1, 2, 3])

    def test_negative(self):
        self.assertNotEqual(self.solution.buildArray([5, 0, 1, 2, 3, 4]), [4, 5, 0, 1, 2, 4])


if __name__ == '__main__':
    main()
