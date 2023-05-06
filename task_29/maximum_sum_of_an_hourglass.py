# You are given an m x n integer matrix grid.
#
# We define an hourglass as a part of the matrix with the following form:
#     [
#         ["A", "B", "C"],
#         ["", "D", ""],
#         ["E", "F", "G"]
#     ]
#
# Return the maximum sum of the elements of an hourglass.
#
# Note that an hourglass cannot be rotated and must be entirely contained within the matrix.
#
# Example 1:
# Input: grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]
# Output: 30
# Explanation: The cells shown above represent the hourglass with the maximum sum: 6 + 2 + 1 + 2 + 9 + 2 + 8 = 30.
#
# Example 2:
# Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
# Output: 35
# Explanation: There is only one hourglass in the matrix, with the sum: 1 + 2 + 3 + 5 + 7 + 8 + 9 = 35.
# Constraints:
# m == grid.length
# n == grid[i].length
# 3 <= m, n <= 150
# 0 <= grid[i][j] <= 106
from typing import List


class SolutionOne:

    def maxSum(self, grid: List[List[int]]) -> int:

        hourglass = [["A", "B", "C"],
                     ["", "D", ""],
                     ["E", "F", "G"]]

        return sum([grid[hourglass.index(elements)][element] for elements in hourglass
                    for element in range(len(elements)) if elements[element]])


class SolutionTwo:

    def maxSum(self, grid: List[List[int]]) -> int:

        hourglass = [["A", "B", "C"],
                     ["", "D", ""],
                     ["E", "F", "G"]]

        counter = 0

        for elements in hourglass:
            for element in range(len(elements)):
                if elements[element]:
                    counter += grid[hourglass.index(elements)][element]

        return counter

