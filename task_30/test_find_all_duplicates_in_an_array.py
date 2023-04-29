from unittest import TestCase, main
from task_30.find_all_duplicates_in_an_array import Solution


class FindDuplicates(TestCase):
    solution = Solution()

    def test_one_positive(self):
        self.assertEqual(self.solution.findDuplicates(nums=[4, 3, 2, 7, 8, 2, 3, 1]),
                         [2, 3])


    def test_two_positive(self):

        self.assertEqual(self.solution.findDuplicates(nums=[1, 1, 2]),
                         [1])


    def test_three_positive(self):

        self.assertEqual(self.solution.findDuplicates(nums=[1]),
                         [])


    def test_negative(self):
        self.assertNotEqual(self.solution.findDuplicates(nums=[1, 7, 1, 3, 4, 7, 1]), [1])



if __name__ == '__main__':
    main()