from typing import List

# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/


class Solution:
    def arrayStringsAreEqualNew(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)

    def arrayStringsAreEqual(self, word1:List[str], word2:List[str]) -> bool:
        word1Index = 0
        word2Index = 0
        word1IndexIndex = 0
        word2IndexIndex = 0
        while True:
            w1 = word1[word1Index][word1IndexIndex]
            w2 = word2[word2Index][word2IndexIndex]
            if w1 != w2:
                return False
            else:
                word1IndexIndex = word1IndexIndex + 1
                word2IndexIndex = word2IndexIndex + 1
                if word1IndexIndex >= len(word1[word1Index]):
                    word1Index = word1Index + 1
                    word1IndexIndex = 0
                if word2IndexIndex >= len(word2[word2Index]):
                    word2Index = word2Index + 1
                    word2IndexIndex = 0
                # If either of one have reached end of string , return false
                if (word1Index >= len(word1) and word2Index < len(word2)) or \
                    (word1Index < len(word1) and word2Index >= len(word2)):
                    return False
                # If both have reached end of line
                elif (word1Index >= len(word1) and word2Index >= len(word2)):
                    return True
                continue

        return True


sol = Solution()
lword1 = ["a,", "b"]
lword2 = ["a,bc"]
print(sol.arrayStringsAreEqual(lword1, lword2))
print(sol.arrayStringsAreEqualNew(lword1, lword2))


