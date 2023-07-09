from unittest import TestCase, main
from task_14.count_the_digits_that_divide_a_number import SolutionOne


class CountDigitsTest(TestCase):
    solution_one = SolutionOne()

    def test_one_positive(self):
        self.assertEqual(self.solution_one.countDigits(7), 1)

    def test_two_positive(self):
        self.assertEqual(self.solution_one.countDigits(121), 2)

    def test_three_positive(self):
        self.assertEqual(self.solution_one.countDigits(1248), 4)


    def test_negative(self):
        self.assertNotEqual(self.solution_one.countDigits(15), 3)


if __name__ == '__main__':
    main()