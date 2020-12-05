# https://leetcode.com/problems/squares-of-a-sorted-array/
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_list = list()
        i = 0
        j = len(nums)-1
        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                new_list.append(nums[i]*nums[i])
                i += 1
            else:
                new_list.append(nums[j] * nums[j])
                j -= 1
        return new_list[::-1]


sol = Solution()

mynums = [-4,-1,0,3,10]
print(sol.sortedSquares(mynums))

mynums = [-7,-3,2,3,11]
print(sol.sortedSquares(mynums))