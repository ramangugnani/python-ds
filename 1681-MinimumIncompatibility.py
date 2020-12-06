# https://leetcode.com/problems/minimum-incompatibility/

from itertools import permutations
from typing import List
import math

class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        k = len(nums) // k
        perm = permutations(nums)
        final_incompatibility = math.inf
        for tuple in list(perm):
            #print(tuple)
            i = 0
            mylist = list(tuple)
            total_incompatibility = 0

            while i < len(mylist):
                small_list = mylist[i:i+k]
                #print(small_list)
                i = i + k
                if len(small_list) == len(set(small_list)):
                    small_list.sort()
                    my_min = small_list[0]
                    my_max = small_list[k-1]
                    incompatibility = my_max - my_min
                    #print(incompatibility)
                    total_incompatibility += incompatibility
                else:
                    total_incompatibility = -1
                    break
            #print(final_incompatibility)
            #print(total_incompatibility)
            if total_incompatibility >= 0:
                final_incompatibility = min(final_incompatibility,total_incompatibility)
            print(final_incompatibility)
        if final_incompatibility == math.inf:
            final_incompatibility = -1
        return final_incompatibility

sol = Solution()
#print(sol.minimumIncompatibility([1,2,1,4], 2))
#print(sol.minimumIncompatibility([6,3,8,1,3,1,2,2], 4))
#print(sol.minimumIncompatibility([5,3,3,6,3,3], 3))
print(sol.minimumIncompatibility([1], 1))