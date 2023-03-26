from unittest import TestCase, main
from task_13.goal_parser_interpretation import Solution


class GoalParserInterpretationTest(TestCase):

    def test_one_positive(self):
        self.assertEqual(Solution.interpret(self, "G()(al)"), "Goal")

    def test_two_positive(self):
        self.assertEqual(Solution.interpret(self, "G()()()()(al)"), "Gooooal")

    def test_three_positive(self):
        self.assertEqual(Solution.interpret(self, "(al)G(al)()()G"), "alGalooG")


    def test_negative(self):
        self.assertNotEqual(Solution.interpret(self, "()()G(al)()()G"), "oGalooG")


if __name__ == '__main__':
    main()