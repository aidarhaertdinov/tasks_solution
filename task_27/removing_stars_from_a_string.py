# You are given a string s, which contains stars *.
#
# In one operation, you can:
#
# Choose a star in s.
# Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.
#
# Note:
#
# The input will be generated such that the operation is always possible.
# It can be shown that the resulting string will always be unique.
#
# Example 1:
# Input: s = "leet**cod*e"
# Output: "lecoe"
# Explanation: Performing the removals from left to right:
# - The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
# - The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
# - The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
# There are no more stars, so we return "lecoe".
#
# Example 2:
# Input: s = "erase*****"
# Output: ""
# Explanation: The entire string is removed, so we return an empty string.
#
#
# Constraints:
# 1 <= s.length <= 105
# s consists of lowercase English letters and stars *.
# The operation above can be performed on s.

from decorator import function_execution_time

class SolutionOne:
    @function_execution_time
    def removeStars(self, s: str) -> str:
        list_s = list(s)
        while "*" in list_s:
            for el in range(len(list_s)):
                if list_s[el] == "*":
                    del list_s[el - 1:el + 1]
                    break

        return ''.join(list_s)


class SolutionTwo:

    def delStar(self, _list: list) -> list:
        if '*' in _list:
            index = _list.index('*')
            del _list[index - 1:index + 1]
            self.delStar(_list)

        return _list

    @function_execution_time
    def removeStars(self, s: str) -> str:
        _list = list(s)

        self.delStar(_list)

        return ''.join(_list)


class SolutionThree:

    def searchIndexByStartPosition(self, _list: list, start_index: int, el: str):
        for index, element in enumerate(_list[start_index:]):
            if el is element:
                return index

    def delStar(self, _list: list, start_index: int) -> list:
        start_index = self.searchIndexByStartPosition(_list, start_index, '*')

        if start_index is None:
            return _list

        del _list[start_index - 1:start_index + 1]

        start_index -= 5

        self.delStar(_list, start_index)

        return _list

    @function_execution_time
    def removeStars(self, s: str) -> str:
        _list = list(s)

        self.delStar(_list, 0)

        return ''.join(_list)


if __name__ == '__main__':

    result = SolutionOne()
    print(result.removeStars(s="leet**cod*e"*100))


    result = SolutionTwo()
    print(result.removeStars(s="leet**cod*e"*100))

    result = SolutionThree()
    print(result.removeStars(s="leet**cod*e" * 100))