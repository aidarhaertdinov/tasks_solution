from unittest import TestCase, main
from task_43.find_all_lonely_numbers_in_the_array import Solution


class FindLonelyTest(TestCase):
    solution = Solution()

    def test_one_positive(self):
        self.assertEqual(self.solution.findLonely(nums=[10, 6, 5, 8]),
                         [10, 8])


    def test_two_positive(self):
        self.assertEqual(self.solution.findLonely(nums=[1, 3, 5, 3]),
                         [1, 5])


    def test_negative(self):
        self.assertNotEqual(self.solution.findLonely(nums=[4, 2, 1, 3, 7, 11, 4, 6]),
                            [1])


if __name__ == '__main__':
    main()
