from typing import List

# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        else:
            result = ""
            for i in range(0,len(strs[0])):
                alphabect = strs[0][i]
                for j in range(1,len(strs)) :
                    if len(strs[j]) < i + 1 or alphabect != strs[j][i]:
                        return result
                result = result + alphabect
            return result


    def longestCommonPrefixNew(self, strs: List[str]) -> str:
        res = ""
        if not strs:
            return res
        # returns the iterator to list of tuples
        for i in zip(*strs):
            print(type(i))
            print(i)
            if len(set(i)) == 1:
                res += i[0]
            else:
                break
        return res



sol = Solution()
strInput = ["flower", "flow", "flight"]
#print(sol.longestCommonPrefix(strInput))
print(sol.longestCommonPrefixNew(strInput))