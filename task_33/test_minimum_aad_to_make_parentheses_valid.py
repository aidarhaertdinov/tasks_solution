from unittest import TestCase, main
from task_33.minimum_aad_to_make_parentheses_valid import Solution


class MinAddToMakeValidTest(TestCase):
    solution = Solution()

    def test_one_positive(self):
        self.assertEqual(self.solution.minAddToMakeValid(s="())"), 1)


    def test_two_positive(self):

        self.assertEqual(self.solution.minAddToMakeValid(s="((("), 3)


    def test_three_positive(self):

        self.assertEqual(self.solution.minAddToMakeValid(s="((())))"), 1)


    def test_negative(self):
        self.assertNotEqual(self.solution.minAddToMakeValid(s="()))"), 3)



if __name__ == '__main__':
    main()