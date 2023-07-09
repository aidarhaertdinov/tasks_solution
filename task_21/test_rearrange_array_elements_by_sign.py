from unittest import TestCase, main
from task_21.rearrange_array_elements_by_sign import Solution


class CountDigitsTest(TestCase):
    solution = Solution()

    def test_one_positive(self):
        self.assertEqual(self.solution.rearrangeArray(nums=[3, 1, -2, -5, 2, -4]),
                         [3, -2, 1, -5, 2, -4])


    def test_two_positive(self):
        self.assertEqual(self.solution.rearrangeArray(nums=[-1, 1]),
                         [1, -1])


    def test_negative(self):
        self.assertNotEqual(self.solution.rearrangeArray(nums=[-1, 2, -5, 4, 3, -3]),
                            [2, -1, 4, -5, -3, 3])



if __name__ == '__main__':
    main()