# You're given strings jewels representing the types of stones that are jewels,
# and stones representing the stones you have. Each character in stones is a type of stone you have.
# You want to know how many of the stones you have are also jewels.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Example 1:

# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3


# Example 2:

# Input: jewels = "z", stones = "ZZ"
# Output: 0

from decorator import function_execution_time


class SolutionOne:
    @function_execution_time
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0
        for jewel in jewels:
            for stone in stones:
                if jewel == stone:
                    counter += 1

        return counter


class SolutionTwo:
    @function_execution_time
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        return sum([stones.count(jewel) for jewel in jewels])




if __name__ == '__main__':

    result = SolutionOne()
    print(result.numJewelsInStones("aA", "aAAbbbb" * 10000000))


    result = SolutionTwo()
    print(result.numJewelsInStones("aA", "aAAbbbb" * 10000000))