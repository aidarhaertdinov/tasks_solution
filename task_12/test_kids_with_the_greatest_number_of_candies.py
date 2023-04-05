from unittest import TestCase, main
from task_12.kids_with_the_greatest_number_of_candies import SolutionOne


class KidsWithCandiesTest(TestCase):

    def test_one_positive(self):
        self.assertEqual(SolutionOne.kidsWithCandies(self, [2, 3, 5, 1, 3], 3),
                         [True, True, True, False, True])

    def test_two_positive(self):
        self.assertEqual(SolutionOne.kidsWithCandies(self, [4, 2, 1, 1, 2], 1),
                         [True, False, False, False, False])

    def test_negative(self):
        self.assertNotEqual(SolutionOne.kidsWithCandies(self, [2, 4, 3, 8], 3), [False, False, True, True])


if __name__ == '__main__':
    main()