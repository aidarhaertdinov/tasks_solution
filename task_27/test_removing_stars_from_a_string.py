from unittest import TestCase, main
from task_27.removing_stars_from_a_string import SolutionOne, SolutionTwo


class RemoveStarsTest(TestCase):
    solution_one = SolutionOne()
    solution_two = SolutionTwo()

    def test_one_positive(self):
        self.assertEqual(self.solution_one.removeStars(s="leet**cod*e"), "lecoe")


    def test_two_positive(self):
        self.assertEqual(self.solution_two.removeStars(s="erase*****"), "")


    def test_one_negative(self):
        self.assertNotEqual(self.solution_one.removeStars(s="no*de**"), "no")


    def test_two_negative(self):
        self.assertNotEqual(self.solution_two.removeStars(s="no*de**"), "no")


if __name__ == '__main__':
    main()