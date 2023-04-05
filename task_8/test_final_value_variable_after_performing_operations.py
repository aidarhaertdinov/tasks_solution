from unittest import TestCase, main
from task_8.final_value_variable_after_performing_operations import SolutionOne


class FinalValueVariableTest(TestCase):

    def test_one(self):
        self.assertEqual(SolutionOne.finalValueAfterOperations(self, ["--X", "X++", "X++"]), 1)

    def test_two(self):
        self.assertEqual(SolutionOne.finalValueAfterOperations(self, ["++X", "++X", "X++"]), 3)

    def test_three(self):
        self.assertEqual(SolutionOne.finalValueAfterOperations(self, ["X++", "++X", "--X", "X--"]), 0)



if __name__ == '__main__':
    main()