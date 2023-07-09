from unittest import TestCase, main
from task_10.subtract_product_and_sum_of_digits_of_an_integer import Solution


class SubtractProductAndSumTest(TestCase):
    solution = Solution()

    def test_one_positive(self):
        self.assertEqual(self.solution.subtractProductAndSum(234), 15)

    def test_two_positive(self):
        self.assertEqual(self.solution.subtractProductAndSum(4421), 21)

    def test_one_negative(self):
        self.assertNotEqual(self.solution.subtractProductAndSum(4421), 24)


if __name__ == '__main__':
    main()