from typing import List

# https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.dc = {-1:0}
        for i in range(0, len(nums)):
            self.dc[i] = self.dc[i-1] + nums[i]
        print(self.dc)

    def sumRange(self, i: int, j: int) -> int:
        return self.dc[j] - self.dc[i-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

myList = [-2, 0, 3, -5, 2, -1]
sol= NumArray(myList)
print(sol.sumRange(0, 2))