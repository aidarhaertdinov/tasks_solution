from unittest import TestCase, main
from task_20.merge_nodes_in_between_zeros import Solution


class CountDigitsTest(TestCase):

    def test_one_positive(self):
        self.assertEqual(Solution.mergeNodes(self, head=[0, 3, 1, 0, 4, 5, 2, 0]), [4, 11])


    def test_two_positive(self):
        self.assertEqual(Solution.mergeNodes(self, head=[0, 1, 0, 3, 0, 2, 2, 0]), [1, 3, 4])


    def test_negative(self):
        self.assertNotEqual(Solution.mergeNodes(self, head=[0, 1, 2, 0, 5, 0, 1, 1, 0]), [2, 5, 2])



if __name__ == '__main__':
    main()