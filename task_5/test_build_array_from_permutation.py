from unittest import TestCase, main
from task_5.build_array_from_permutation import Solution


class BuildArrayPermutationTest(TestCase):

    def test_one(self):
        self.assertEqual(Solution.buildArray(self, [0,2,1,5,3,4]), [0,1,2,4,5,3])

    def test_two(self):
        self.assertEqual(Solution.buildArray(self, [5,0,1,2,3,4]), [4,5,0,1,2,3])


if __name__ == '__main__':
    main()
