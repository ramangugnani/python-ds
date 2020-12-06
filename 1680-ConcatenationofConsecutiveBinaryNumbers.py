# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

import math

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = 0
        for i in range(1,n+1):
            shift = int(math.log2(i)) + 1
            ans = (ans << shift) + i
            ans = ans % (10**9 + 7)
        return ans % (10**9 + 7)


sol = Solution()

#print(sol.concatenatedBinary(1))

#print(sol.concatenatedBinary(3))

print(sol.concatenatedBinary(88006))
