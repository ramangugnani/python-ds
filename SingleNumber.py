from typing import List

# https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums : List[int]) -> int:
        result = 0
        for i in nums:
            result = result ^ i
        return result

sol= Solution()
mylist = [1,2,1]
print(sol.singleNumber(mylist))