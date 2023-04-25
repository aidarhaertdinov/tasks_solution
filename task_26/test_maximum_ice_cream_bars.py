from unittest import TestCase, main
from task_26.maximum_ice_cream_bars import Solution


class MaxIceCreamTest(TestCase):

    def test_one_positive(self):
        self.assertEqual(Solution.maxIceCream(self, costs=[1, 3, 2, 4, 1], coins=7), 4)


    def test_two_positive(self):
        self.assertEqual(Solution.maxIceCream(self, costs=[10, 6, 8, 7, 7, 8], coins=5), 0)


    def test_three_positive(self):
        self.assertEqual(Solution.maxIceCream(self, costs=[1, 6, 3, 1, 2, 5], coins=20), 6)


    def test_negative(self):
        self.assertNotEqual(Solution.maxIceCream(self, costs=[10, 6, 11, 7, 9, 8], coins=6), 2)



if __name__ == '__main__':
    main()