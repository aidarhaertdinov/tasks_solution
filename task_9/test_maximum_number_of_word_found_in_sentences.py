from unittest import TestCase, main
from task_9.maximum_number_of_word_found_in_sentences import SolutionOne


class MaximumNumberWordTest(TestCase):

    def test_one(self):
        self.assertEqual(SolutionOne.mostWordsFound(self,
                                                    ["alice and bob love leetcode", "i think so too",
                                                  "this is great thanks very much"]), 6)

    def test_two(self):
        self.assertEqual(SolutionOne.mostWordsFound(self, ["please wait", "continue to fight", "continue to win"]), 3)


if __name__ == '__main__':
    main()