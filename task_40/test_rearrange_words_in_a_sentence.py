from unittest import TestCase, main
from task_40.rearrange_words_in_a_sentence import Solution


class ArrangeWordsTest(TestCase):
    solution = Solution()

    def test_one_positive(self):
        self.assertEqual(self.solution.arrangeWords(text="Leetcode is cool"),
                         "Is cool leetcode")


    def test_two_positive(self):
        self.assertEqual(self.solution.arrangeWords(text="Keep calm and code on"),
                         "On and keep calm code")


    def test_negative(self):
        self.assertNotEqual(self.solution.arrangeWords(text="Python is amazing"),
                            "is Python amazing")


if __name__ == '__main__':
    main()
