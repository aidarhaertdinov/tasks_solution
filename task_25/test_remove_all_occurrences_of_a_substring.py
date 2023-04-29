from unittest import TestCase, main
from task_25.remove_all_occurrences_of_a_substring import Solution


class RemoveAllOccurrencesTest(TestCase):

    def test_one_positive(self):
        solution = Solution()
        self.assertEqual(solution.removeOccurrences(s="daabcbaabcbc", part="abc"),
                         "dab")

    #
    # def test_two_positive(self):
    #     self.assertEqual(Solution.removeOccurrences(self, s="axxxxyyyyb", part="xy"),
    #                      "ab")
    #
    #
    # def test_negative(self):
    #     self.assertNotEqual(Solution.removeOccurrences(self, s="xciacia", part="ci"), "xia")



if __name__ == '__main__':
    main()