from unittest import TestCase, main
from task_35.validate_stack_sequences import Solution


class ValidateStackSequencesTest(TestCase):
    solution = Solution()

    def test_one_positive(self):
        self.assertEqual(self.solution.validateStackSequences(pushed=[1, 2, 3, 4, 5],
                                                              popped=[4, 5, 3, 2, 1]), True)

    def test_two_positive(self):
        self.assertEqual(self.solution.validateStackSequences(pushed=[1, 2, 3, 4, 5],
                                                              popped=[4, 3, 5, 1, 2]), False)

    def test_three_positive(self):
        self.assertEqual(self.solution.validateStackSequences(pushed=[2, 1, 0],
                                                              popped=[1, 2, 0]), True)

    def test_negative(self):
        self.assertNotEqual(self.solution.validateStackSequences(pushed=[3, 4, 5, 7, 8],
                                                                 popped=[8, 7, 6, 4, 3]), True)


if __name__ == '__main__':
    main()
