from unittest import TestCase, main
from task_42.sort_characters_by_frequency import Solution


class MinCostTest(TestCase):
    solution = Solution()

    def test_one_positive(self):
        self.assertEqual(self.solution.frequencySort(s="tree"), "eetr")


    def test_three_positive(self):
        self.assertEqual(self.solution.frequencySort(s="Aabb"), "bbAa")


    def test_negative(self):
        self.assertNotEqual(self.solution.frequencySort(s="lleetelloovvdt"), "dlllleeevvoott")


if __name__ == '__main__':
    main()
