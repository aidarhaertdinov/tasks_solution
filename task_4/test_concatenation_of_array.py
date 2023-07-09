from unittest import TestCase, main
from task_4.concatenation_of_array import Solution


class ConcatenationArrayTest(TestCase):
    solution = Solution()

    def test_one_positive(self):
        self.assertEqual(self.solution.getConcatenation([1, 2, 1]), [1, 2, 1, 1, 2, 1])

    def test_two_positive(self):
        self.assertEqual(self.solution.getConcatenation([1, 3, 2, 1]), [1, 3, 2, 1, 1, 3, 2, 1])


    def test_negative(self):
        self.assertNotEqual(self.solution.getConcatenation([1, 3, 2, 1]), [1, 3, 4, 1, 1, 3, 2, 1])


if __name__ == '__main__':
    main()
