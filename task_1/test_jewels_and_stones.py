from unittest import TestCase, main
from task_1.jewels_and_stones771 import Solution


class JewelStonesTest(TestCase):

    def test_one(self):
        self.assertEqual(Solution.numJewelsInStones(self, "aA", "aAAbbbb"), 3)

    def test_two(self):
        self.assertEqual(Solution.numJewelsInStones(self, "z", "ZZ"), 0)


if __name__ == '__main__':
    main()
