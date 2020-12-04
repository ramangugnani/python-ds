# https://leetcode.com/problems/reverse-integer/

maxNum = 2 ** 31 - 1
minNum = -2 ** 31

class Solution:

    def reverse(self, x: int) -> int:
        if x >= 0:
            reverse_num = int(str(x)[::-1])
        else:
            reverse_num = -1*int(str(x*-1)[::-1])

        global maxNum
        global minNum
        if reverse_num > maxNum or reverse_num < minNum:
            return 0
        else:
            return reverse_num


sol = Solution()
print(sol.reverse(-123))
