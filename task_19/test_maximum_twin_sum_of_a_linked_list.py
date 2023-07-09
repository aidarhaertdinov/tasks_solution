from unittest import TestCase, main
from task_19.maximum_twin_sum_of_a_linked_list import Solution


class CountDigitsTest(TestCase):
    solution = Solution()

    def test_one_positive(self):
        self.assertEqual(self.solution.pairSum(head=[5, 4, 2, 1]), 6)


    def test_two_positive(self):
        self.assertEqual(self.solution.pairSum(head=[4, 2, 2, 3]), 7)


    def test_three_positive(self):
        self.assertEqual(self.solution.pairSum(head=[1, 100000]), 100001)


    def test_negative(self):
        self.assertNotEqual(self.solution.pairSum(head=[5, 3, 1, 0]), 4)



if __name__ == '__main__':
    main()