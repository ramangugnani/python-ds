# https://leetcode.com/problems/binary-search/
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return -1


sol = Solution()

print(sol.search([-1,0,3,5,9,12], 9))

print(sol.search([-1,0,3,5,9,12], 2))
