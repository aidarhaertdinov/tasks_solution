from unittest import TestCase, main
from task_1.jewels_and_stones771 import SolutionOne, SolutionTwo


class JewelStonesTest(TestCase):
    solution = SolutionOne()

    def test_one_positive(self):
        self.assertEqual(self.solution.numJewelsInStones("aA", "aAAbbbb"), 3)

    def test_two_positive(self):
        self.assertEqual(self.solution.numJewelsInStones("z", "ZZ"), 0)

    def test_one_negative(self):
        self.assertNotEqual(self.solution.numJewelsInStones("aA", "aAAbbbb"), 2)


if __name__ == '__main__':
    main()
