from unittest import TestCase, main
from task_29.maximum_sum_of_an_hourglass import SolutionOne


class MaxSum(TestCase):
    solution = SolutionOne()

    def test_one_positive(self):
        self.assertEqual(self.solution.maxSum(grid=[[6, 2, 1, 3], [4, 2, 1, 5], [9, 2, 8, 7], [4, 1, 2, 9]]),
                         30
                         )


    def test_two_positive(self):

        self.assertEqual(self.solution.maxSum(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                         35
                         )


    def test_negative(self):
        self.assertNotEqual(self.solution.maxSum(grid=[[5, 1, 5], [7, 2, 9], [3, 6, 6]]),
                            29
                            )



if __name__ == '__main__':
    main()