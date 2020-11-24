from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for counter, value in enumerate(nums):
            remaining = target - value
            if remaining in dictionary:
                return [counter, dictionary[remaining]]
            dictionary[value] = counter
        return []


sol= Solution()
nums = [1,2,3,5]
target = 5
ans = sol.twoSum(nums,target)
print(ans)