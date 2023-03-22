from unittest import TestCase, main
from task_4.concatenation_of_array import Solution


class ConcatenationArrayTest(TestCase):

    def test_one(self):
        self.assertEqual(Solution.getConcatenation(self, [1,2,1]), [1,2,1,1,2,1])

    def test_two(self):
        self.assertEqual(Solution.getConcatenation(self, [1,3,2,1]), [1,3,2,1,1,3,2,1])


if __name__ == '__main__':
    main()
