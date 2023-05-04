from unittest import TestCase, main
from task_34.sort_integers_by_the_power_value import Solution


class SortIntegersTest(TestCase):
    solution = Solution()

    def test_one_positive(self):
        self.assertEqual(self.solution.getKth(lo=12, hi=15, k=2), 13)


    def test_two_positive(self):

        self.assertEqual(self.solution.getKth(lo=7, hi=11, k=4), 7)


    def test_negative(self):
        self.assertNotEqual(self.solution.getKth(lo=7, hi=11, k=4), 3)



if __name__ == '__main__':
    main()