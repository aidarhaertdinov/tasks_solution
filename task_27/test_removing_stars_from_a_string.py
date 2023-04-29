from unittest import TestCase, main
from task_27.removing_stars_from_a_string import Solution


class RemoveStarsTest(TestCase):

    def test_one_positive(self):
        self.assertEqual(Solution.removeStars(self, s="leet**cod*e"), "lecoe")


    def test_two_positive(self):
        self.assertEqual(Solution.removeStars(self, s="erase*****"), "")


    def test_negative(self):
        self.assertNotEqual(Solution.removeStars(self, s="no*de**"), "no")



if __name__ == '__main__':
    main()