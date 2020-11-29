from typing import List

# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums : List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[1]
        else:
            mylist = dict()
            mylist[-1] = 0
            mylist[0] = nums[0]
            for i in range(1,len(nums)):
                mylist[i] = max(mylist[i-1],mylist[i-2]+nums[i])
            return mylist.get(len(nums)-1)


sol = Solution()
numbers = [1, 2, 3, 1]
print(sol.rob(numbers))
