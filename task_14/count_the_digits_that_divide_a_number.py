# Given an integer num, return the number of digits in num that divide num.
#
# An integer val divides nums if nums % val == 0.
#
# Example 1:
#
# Input: num = 7
# Output: 1
# Explanation: 7 divides itself, hence the answer is 1.
# Example 2:
#
# Input: num = 121
# Output: 2
# Explanation: 121 is divisible by 1, but not 2. Since 1 occurs twice as a digit, we return 2.
# Example 3:
#
# Input: num = 1248
# Output: 4
# Explanation: 1248 is divisible by all of its digits, hence the answer is 4.
#
#
# Constraints:
#
# 1 <= num <= 109
# num does not contain 0 as one of its digits.

from decorator import function_execution_time


class SolutionOne:

    @function_execution_time
    def countDigits(self, num: int) -> int:
        counter = 0
        for i in str(num):
            if num % int(i) == 0:
                counter += 1

        return counter


class SolutionTwo:

    @function_execution_time
    def countDigits(self, num: int) -> int:

        return sum([1 for i in str(num) if num % int(i) == 0])


if __name__ == '__main__':
    result = SolutionOne()
    print(result.countDigits(121))


    result = SolutionTwo()
    print(result.countDigits(121))