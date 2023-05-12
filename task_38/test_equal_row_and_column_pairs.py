from unittest import TestCase, main
from task_38.equal_row_and_column_pairs import Solution


class EqualPairsTest(TestCase):
    solution = Solution()

    def test_one_positive(self):
        self.assertEqual(self.solution.equalPairs(grid=[[3, 2, 1],
                                                        [1, 7, 6],
                                                        [2, 7, 7]]),
                         1)

    def test_two_positive(self):
        self.assertEqual(self.solution.equalPairs(grid=[[3, 1, 2, 2],
                                                        [1, 4, 4, 5],
                                                        [2, 4, 2, 2],
                                                        [2, 4, 2, 2]]),
                         3)

    def test_negative(self):
        self.assertNotEqual(self.solution.equalPairs(grid=[[3, 2, 1],
                                                           [1, 7, 6],
                                                           [2, 7, 7]]),
                            2)


if __name__ == '__main__':
    main()
