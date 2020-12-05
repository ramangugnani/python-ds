# https://leetcode.com/problems/majority-element/
from typing import List

class Solution:
    def majorityElement(self, nums : List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]


sol = Solution()
mylist = [3,2,3]
print(sol.majorityElement(mylist))
mylist = [1,2,1,1,1,2,2]
print(sol.majorityElement(mylist))