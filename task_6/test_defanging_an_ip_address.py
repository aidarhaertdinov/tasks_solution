from unittest import TestCase, main
from task_6.defanging_an_ip_address import Solution


class DefendingIpAddressTest(TestCase):
    solution = Solution()

    def test_one_positive(self):
        self.assertEqual(self.solution.defangIPaddr("1.1.1.1"), "1[.]1[.]1[.]1")

    def test_two_positive(self):
        self.assertEqual(self.solution.defangIPaddr("255.100.50.0"), "255[.]100[.]50[.]0")


    def test_negative(self):
        self.assertNotEqual(self.solution.defangIPaddr("255.100.50.0"), "255[.]100[.]70[.]0")


if __name__ == '__main__':
    main()
