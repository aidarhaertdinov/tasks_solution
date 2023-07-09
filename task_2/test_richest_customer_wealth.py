from unittest import TestCase, main
from task_2.richest_customer_wealth import SolutionOne


class RichestCustomerTest(TestCase):
    solution = SolutionOne()

    def test_one_positive(self):
        self.assertEqual(self.solution.maximumWealth([[1, 2, 3], [3, 2, 1]]), 6)


    def test_two_positive(self):
        self.assertEqual(self.solution.maximumWealth([[1, 5], [7, 3], [3, 5]]), 10)


    def test_three_positive(self):
        self.assertEqual(self.solution.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]), 17)


    def test_negative(self):
        self.assertNotEqual(self.solution.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]), 13)


if __name__ == '__main__':
    main()