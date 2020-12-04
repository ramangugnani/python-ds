# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self,x: int) -> bool:
        # -ve number can't be palindrome
        if x < 0:
            return False
        # zero is anyways palindrome
        elif x == 0:
            return True
        else:
            # Number with zero in last is will be not be a palindrome
            if x % 10 == 0:
                return False
            y = 0
            # Lets reverse the second part of the number
            # Second part is determined when Y becomes greater than X
            while y < x:
                digit = x % 10
                x = int(x / 10)
                y = y * 10 + digit

            # If number is odd then X and Y will be not be same
            # In that case we need to omit the last digit in Y and verify
            if x == y or x == int(y/10):
                return True
            else:
                return False

s = Solution()
print(s.isPalindrome(10))