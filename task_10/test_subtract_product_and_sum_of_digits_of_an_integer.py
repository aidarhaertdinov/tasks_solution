from unittest import TestCase, main
from task_10.subtract_product_and_sum_of_digits_of_an_integer import Solution


class SubtractProductAndSumTest(TestCase):

    def test_one(self):
        self.assertEqual(Solution.subtractProductAndSum(self, 234), 15)

    def test_two(self):
        self.assertEqual(Solution.subtractProductAndSum(self, 4421), 21)


if __name__ == '__main__':
    main()