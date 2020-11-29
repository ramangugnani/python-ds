from typing import  List

# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumer(self, nums: List[int]) -> int:
        result = 0
        i = 0
        res = 0
        for num in nums:
            result = result ^ num
            res = res ^ i
            i += 1

        result = result ^ res ^ i
        return result


sol = Solution()
numbers = [0,1,2,3]
print(sol.missingNumer(numbers))