from unittest import TestCase, main
from task_8.final_value_variable_after_performing_operations import SolutionOne


class FinalValueVariableTest(TestCase):
    solution = SolutionOne()

    def test_one_positive(self):
        self.assertEqual(self.solution.finalValueAfterOperations(["--X", "X++", "X++"]), 1)

    def test_two_positive(self):
        self.assertEqual(self.solution.finalValueAfterOperations(["++X", "++X", "X++"]), 3)

    def test_three_positive(self):
        self.assertEqual(self.solution.finalValueAfterOperations(["X++", "++X", "--X", "X--"]), 0)

    def test_negative(self):
        self.assertNotEqual(self.solution.finalValueAfterOperations(["X++", "++X", "--X", "X--"]), 4)


if __name__ == '__main__':
    main()