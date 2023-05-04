from unittest import TestCase, main
from task_31.rotate_image import Solution


class RotateTest(TestCase):
    solution = Solution()

    def test_one_positive(self):
        self.assertEqual(self.solution.rotate(matrix=[[1, 2, 3],
                                                      [4, 5, 6],
                                                      [7, 8, 9]]),
                         [[7, 4, 1],
                          [8, 5, 2],
                          [9, 6, 3]])

    def test_two_positive(self):
        self.assertEqual(self.solution.rotate(matrix=[[5, 1, 9, 11],
                                                      [2, 4, 8, 10],
                                                      [13, 3, 6, 7],
                                                      [15, 14, 12, 16]]),
                         [[15, 13, 2, 5],
                          [14, 3, 4, 1],
                          [12, 6, 8, 9],
                          [16, 7, 10, 11]])

    def test_negative(self):
        self.assertNotEqual(self.solution.rotate(matrix=[[3, 8, 9],
                                                         [4, 4, 2],
                                                         [3, 3, 5],
                                                         [5, 4, 2]]),
                            [[5, 3, 4, 3],
                             [2, 5, 2, 9],
                             [4, 3, 4, 8]])


if __name__ == '__main__':
    main()
