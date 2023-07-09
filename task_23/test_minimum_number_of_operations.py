from unittest import TestCase, main
from task_23.minimum_number_of_operations import Solution


class MinimumNumberTest(TestCase):
    solution = Solution()

    def test_one_positive(self):
        self.assertEqual(self.solution.minOperations(boxes="110"), [1, 1, 3])


    def test_two_positive(self):
        self.assertEqual(self.solution.minOperations(boxes="001011"), [11, 8, 5, 4, 3, 4])


    def test_negative(self):
        self.assertNotEqual(self.solution.minOperations(boxes="01010"), [4, 2, 2, 4, 4])



if __name__ == '__main__':
    main()