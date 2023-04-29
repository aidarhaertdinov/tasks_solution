from unittest import TestCase, main
from task_28.minimum_number_steps_to_make_two_strings_anagram import Solution


class MinSteps(TestCase):
    solution = Solution()

    def test_one_positive(self):
        self.assertEqual(self.solution.minSteps(s="bab", t="aba"), 1)


    def test_two_positive(self):

        self.assertEqual(self.solution.minSteps(s="leetcode", t="practice"), 5)


    def test_three_positive(self):

        self.assertEqual(self.solution.minSteps(s="anagram", t="mangaar"), 0)


    def test_negative(self):
        self.assertNotEqual(self.solution.minSteps(s="bravo", t="vrita"), 1)



if __name__ == '__main__':
    main()