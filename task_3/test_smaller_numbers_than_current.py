from unittest import TestCase, main
from task_3.smaller_numbers_than_current import Solution


class SmallerNumbersThanCurrentTest(TestCase):
    solution = Solution()

    def test_one_positive(self):
        self.assertEqual(self.solution.smallerNumbersThanCurrent([8, 1, 2, 2, 3]), [4, 0, 1, 1, 3])


    def test_two_positive(self):
        self.assertEqual(self.solution.smallerNumbersThanCurrent([6, 5, 4, 8]), [2, 1, 0, 3])


    def test_three_positive(self):
        self.assertEqual(self.solution.smallerNumbersThanCurrent([7, 7, 7, 7]), [0, 0, 0, 0])


    def test_negative(self):
        self.assertNotEqual(self.solution.smallerNumbersThanCurrent([7, 7, 7, 7]), [0, 1, 0, 0])



if __name__ == '__main__':
    main()
