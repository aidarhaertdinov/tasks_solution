from unittest import TestCase, main
from task_9.maximum_number_of_word_found_in_sentences import SolutionOne


class MaximumNumberWordTest(TestCase):
    solution = SolutionOne()

    def test_one_positive(self):
        self.assertEqual(self.solution.mostWordsFound(["alice and bob love leetcode", "i think so too",
                                                  "this is great thanks very much"]), 6)

    def test_two_positive(self):
        self.assertEqual(self.solution.mostWordsFound(["please wait", "continue to fight", "continue to win"]), 3)


    def test_negative(self):
        self.assertNotEqual(self.solution.mostWordsFound(["please wait", "continue to fight", "continue to win"]), 5)



if __name__ == '__main__':
    main()