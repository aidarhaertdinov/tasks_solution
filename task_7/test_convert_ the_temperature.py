from unittest import TestCase, main
from task_7.convert_the_temperature import Solution

class ConvertTemperatureTest(TestCase):
    solution = Solution()

    def test_one_positive(self):
        self.assertEqual(self.solution.convertTemperature(36.50), [309.65000, 97.70000])

    def test_two_positive(self):
        self.assertEqual(self.solution.convertTemperature(122.11), [395.26000, 251.79800])


    def test_negative(self):
        self.assertNotEqual(self.solution.convertTemperature(122.11), [395.26000, 256.79800])


if __name__ == '__main__':
    main()

