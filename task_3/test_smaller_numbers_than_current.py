from unittest import TestCase, main
from task_3.smaller_numbers_than_current import Solution


class SmallerNumbersThanCurrentTest(TestCase):

    def test_one(self):
        self.assertEqual(Solution.smallerNumbersThanCurrent(self, [8, 1, 2, 2, 3]), [4, 0, 1, 1, 3])

    def test_two(self):
        self.assertEqual(Solution.smallerNumbersThanCurrent(self, [6, 5, 4, 8]), [2, 1, 0, 3])

    def test_three(self):
        self.assertEqual(Solution.smallerNumbersThanCurrent(self, [7, 7, 7, 7]), [0, 0, 0, 0])


if __name__ == '__main__':
    main()
