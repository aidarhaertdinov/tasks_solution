from unittest import TestCase, main
from task_14.count_the_digits_that_divide_a_number import SolutionOne


class CountDigitsTest(TestCase):

    def test_one_positive(self):
        self.assertEqual(SolutionOne.countDigits(self, 7), 1)

    def test_two_positive(self):
        self.assertEqual(SolutionOne.countDigits(self, 121), 2)

    def test_three_positive(self):
        self.assertEqual(SolutionOne.countDigits(self, 1248), 4)


    def test_negative(self):
        self.assertNotEqual(SolutionOne.countDigits(self, 15), 3)


if __name__ == '__main__':
    main()