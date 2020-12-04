from typing import List
import  math
# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self,nums : List[int]) -> int:
        globalMax = - math.inf
        previousMax = - math.inf
        for num in nums:
            previousMax = max(num, num + previousMax)
            globalMax = max(globalMax,previousMax)
        return globalMax

sol = Solution()
myList = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(sol.maxSubArray(myList))