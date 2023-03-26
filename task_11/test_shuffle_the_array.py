from unittest import TestCase, main
from task_11.shuffle_the_array import Solution


class ShuffleArrayTest(TestCase):

    def test_one_positive(self):
        self.assertEqual(Solution.shuffle(self, [2, 5, 1, 3, 4, 7], 3), [2, 3, 5, 4, 1, 7])

    def test_two_positive(self):
        self.assertEqual(Solution.shuffle(self, [1, 2, 3, 4, 4, 3, 2, 1], 4), [1, 4, 2, 3, 3, 2, 4, 1])

    def test_negative(self):
        self.assertNotEqual(Solution.shuffle(self, [1, 2, 3, 3, 2, 1], 3), [1, 3, 2, 2, 3, 3])


if __name__ == '__main__':
    main()