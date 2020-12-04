# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n : int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            old = 1
            new = 2
            res = 0
            for i in range(3,n+1):
                res = old + new
                old = new
                new = res
            return res


sol = Solution()
print(sol.climbStairs(2))