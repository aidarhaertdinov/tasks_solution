from unittest import TestCase, main
from task_19_ListNode.maximum_twin_sum_of_a_linked_list import Solution


class CountDigitsTest(TestCase):

    def test_one_positive(self):
        self.assertEqual(Solution.pairSum(self, head=[5, 4, 2, 1]), 6)


    def test_two_positive(self):
        self.assertEqual(Solution.pairSum(self, head=[4, 2, 2, 3]), 7)


    def test_three_positive(self):
        self.assertEqual(Solution.pairSum(self, head=[1, 100000]), 100001)


    def test_negative(self):
        self.assertNotEqual(Solution.pairSum(self, head=[5, 3, 1, 0]), 4)



if __name__ == '__main__':
    main()