from unittest import TestCase, main
from task_2.richest_customer_wealth import Solution


class RichestCustomerTest(TestCase):
     

    def test_one(self):
        self.assertEqual(Solution.maximumWealth(self, [[1, 2, 3], [3, 2, 1]]), 6)


    def test_two(self):
        self.assertEqual(Solution.maximumWealth(self, [[1, 5], [7, 3], [3, 5]]), 10)


    def test_three(self):
        self.assertEqual(Solution.maximumWealth(self, [[2, 8, 7], [7, 1, 3], [1, 9, 5]]), 17)



if __name__ == '__main__':
    main()