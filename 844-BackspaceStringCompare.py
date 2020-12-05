# https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_stack = list()
        t_stack = list()
        for character in S:
            if character is not '#':
                s_stack.append(character)
            else:
                if len(s_stack) > 0:
                    s_stack.pop()

        for character in T:
            if character is not '#':
                t_stack.append(character)
            else:
                if len(t_stack) > 0:
                    t_stack.pop()

        if s_stack == t_stack:
            return True
        else:
            return False

    def backspaceCompareNew(self, S: str, T: str) -> bool:
        i = len(S) - 1
        j = len(T) - 1
        skip_s = 0
        skip_t = 0
        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == "#":
                    skip_s += 1
                    i -= 1
                else:
                    if skip_s > 0:
                        i -= 1
                        skip_s -= 1
                    else:
                        break

            while j >= 0:
                if T[j] == "#":
                    skip_t += 1
                    j -= 1
                else:
                    if skip_t > 0:
                        j -= 1
                        skip_t -= 1
                    else:
                        break

            if i >= 0 and j >= 0:
                if S[i] != T[j]:
                    return False
                else:
                    i -= 1
                    j -= 1
            else:
                break

        if i != j:
            return False
        else:
            return True


sol = Solution()
S = "ab##c"
T = "ad##c"
print(sol.backspaceCompareNew(S,T))

S = "bxj##tw"
T = "bxj###tw"
print(sol.backspaceCompareNew(S,T))
