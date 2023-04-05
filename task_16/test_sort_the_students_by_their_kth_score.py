from unittest import TestCase, main
from task_16.sort_the_students_by_their_kth_score import Solution


class CountDigitsTest(TestCase):

    def test_one_positive(self):
        self.assertEqual(Solution.sortTheStudents(self, [[10, 6, 9, 1], [7, 5, 11, 2],[4, 8, 3, 15]], 2),
                         [[7, 5, 11, 2], [10, 6, 9, 1], [4, 8, 3, 15]])


    def test_two_positive(self):
        self.assertEqual(Solution.sortTheStudents(self, [[3, 4], [5, 6]], 0),
                         [[5, 6], [3, 4]])


    def test_negative(self):
        self.assertNotEqual(Solution.sortTheStudents(self, [[3, 4], [5, 6]], 0),
                         [[5, 6], [3, 5]])


if __name__ == '__main__':
    main()