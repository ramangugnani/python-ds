from typing import List

# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        myset = set(nums)
        mylist = list()
        for i in range(1,len(nums)+1):
            if i not in myset:
                mylist.append(i)
        return mylist


sol = Solution()
input = [3,2,4]
print(sol.findDisappearedNumbers(input))