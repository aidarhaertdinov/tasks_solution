from unittest import TestCase, main
from task_6.defanging_an_ip_address import Solution


class DefendingIpAddressTest(TestCase):

    def test_one(self):
        self.assertEqual(Solution.defangIPaddr(self, "1.1.1.1"), "1[.]1[.]1[.]1")

    def test_two(self):
        self.assertEqual(Solution.defangIPaddr(self, "255.100.50.0"), "255[.]100[.]50[.]0")


if __name__ == '__main__':
    main()
