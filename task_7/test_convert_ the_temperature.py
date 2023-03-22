from unittest import TestCase, main
from task_7.convert_the_temperature import Solution

class ConvertTemperatureTest(TestCase):

    def test_one(self):
        self.assertEqual(Solution.convertTemperature(self, 36.50), [309.65000, 97.70000])

    def test_two(self):
        self.assertEqual(Solution.convertTemperature(self, 122.11), [395.26000, 251.79800])



if __name__ == '__main__':
    main()

