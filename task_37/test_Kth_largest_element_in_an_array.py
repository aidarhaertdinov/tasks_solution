from unittest import TestCase, main
from task_37.Kth_largest_element_in_an_array import Solution


class KthLargestTest(TestCase):
    solution = Solution()

    def test_one_positive(self):
        self.assertEqual(self.solution.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2), 5)

    def test_two_positive(self):
        self.assertEqual(self.solution.findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4), 4)

    def test_negative(self):
        self.assertNotEqual(self.solution.findKthLargest(nums=[3, 2, 1, 5, 6, 4, 7, 0, 4, 5, 6, 7, 2, 3], k=3), 5)


if __name__ == '__main__':
    main()
