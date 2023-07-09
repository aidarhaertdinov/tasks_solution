from unittest import TestCase, main
from task_17.number_of_laser_beams_in_a_bank import Solution


class CountDigitsTest(TestCase):
    solution = Solution()

    def test_one_positive(self):
        self.assertEqual(self.solution.numberOfBeams(["011001", "000000", "010100", "001000"]), 8)


    def test_two_positive(self):
        self.assertEqual(self.solution.numberOfBeams(["000", "111", "000"]), 0)


    def test_negative(self):
        self.assertNotEqual(self.solution.numberOfBeams(["000", "111", "000"]), 3)



if __name__ == '__main__':
    main()