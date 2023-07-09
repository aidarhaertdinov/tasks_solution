from unittest import TestCase, main
from task_22.widest_vertical_area_between_two_points_containing_no_points import Solution


class CountDigitsTest(TestCase):
    solution = Solution()

    def test_one_positive(self):
        self.assertEqual(self.solution.maxWidthOfVerticalArea(points=[[8, 7], [9, 9], [7, 4], [9, 7]]),
                         1)


    def test_two_positive(self):
        self.assertEqual(self.solution.maxWidthOfVerticalArea(points=[[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]),
                        3)


    def test_negative(self):
        self.assertNotEqual(self.solution.maxWidthOfVerticalArea(points=[[2, 9], [7, 4], [9, 7]]),
                            4)



if __name__ == '__main__':
    main()