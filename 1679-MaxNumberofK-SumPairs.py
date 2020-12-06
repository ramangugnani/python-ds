# https://leetcode.com/problems/max-number-of-k-sum-pairs/

from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        my_dict = dict()
        ans = 0
        for num in nums:
            if my_dict.get(num) is not None:
                my_dict[num] = my_dict[num] + 1
            else:
                my_dict[num] = 1
        for num in nums:
            if my_dict.get(num) > 0:
                my_dict[num] = my_dict[num] - 1
                if my_dict.get(k-num) is not None and my_dict.get(k-num) > 0:
                    my_dict[k-num] = my_dict[k-num] - 1
                    ans += 1
        return ans


sol = Solution()
print(sol.maxOperations([1,2,3,4],5))

print(sol.maxOperations([3,1,3,4,3],6))
