# Given two integer arrays pushed and popped each with distinct values, return true if this could
# have been the result of a sequence of push and pop operations on an initially empty stack,
# or false otherwise.
#
# Example 1:
# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4),
# pop() -> 4,
# push(5),
# pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
#
# Example 2:
# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# Output: false
# Explanation: 1 cannot be popped before 2.
#
# Constraints:
# 1 <= pushed.length <= 1000
# 0 <= pushed[i] <= 1000
# All the elements of pushed are unique.
# popped.length == pushed.length
# popped is a permutation of pushed.

from typing import List
# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        new_list = []

        for i in pushed:
            new_list.append(i)

            while new_list[-1] == popped[0]:
                new_list.remove(new_list[-1])
                popped.remove(popped[0])
                if len(new_list) >= 1:
                    continue
                else:
                    break

        if len(new_list):
            return False
        else:
            return True