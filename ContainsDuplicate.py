from typing import List
# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myset = set()
        for number in nums:
            if number in myset:
                return True
            else:
                myset.add(number)
        return False

sol = Solution()
nums = [1,2,3,1]
print(sol.containsDuplicate(nums))