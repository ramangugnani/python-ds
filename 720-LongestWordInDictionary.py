# https://leetcode.com/problems/longest-word-in-dictionary/
from typing import List

class Solution:
    def longestWord(self, words: List[str]) -> str:
        if len(words) == 0:
            return ""

        my_set = set()
        for word in words:
            for i in range(0,26):
                my_set.add(word+chr(97+i))

        #print(my_set)
        my_ans = list()
        max_length = 0
        for word in words:
            if word in my_set:
                if len(word) == max_length:
                    my_ans.append(word)
                elif len(word) > max_length:
                    max_length = len(word)
                    my_ans.clear()
                    my_ans.append(word)

        my_ans.sort()
        #print(my_ans)
        if len(my_ans) > 0:
            return my_ans[0]
        else:
            return ""


sol = Solution()
my_words = ["w","wo","wor","worl", "world"]
print(sol.longestWord(my_words))

my_words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
print(sol.longestWord(my_words))

my_words = ["b","br","bre","brea","break","breakf","breakfa","breakfas","breakfast","l","lu","lun","lunc","lunch","d","di","din","dinn","dinne","dinner"]
print(sol.longestWord(my_words))

my_words = ["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"]
print(sol.longestWord(my_words))
