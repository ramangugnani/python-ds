
# https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    def titleToNumer(self,s: str) -> int:
        s = s[::-1]
        num = 0
        for i in range(0, len(s)):
            num = num + (26**i)*self.getNumber(s[i])
        return num

    def getNumber(self,s:str) -> int:
        if(s == "A"):
            return 1
        elif(s == "B"):
            return  2
        elif(s == "C"):
            return 3
        elif (s == "D"):
            return 4
        elif (s == "E"):
            return 5
        elif (s == "F"):
            return 6
        elif (s == "G"):
            return 7
        elif (s == "H"):
            return 8
        elif (s == "I"):
            return 9
        elif (s == "J"):
            return 10
        elif (s == "K"):
            return 11
        elif (s == "L"):
            return 12
        elif (s == "M"):
            return 13
        elif (s == "N"):
            return 14
        elif (s == "O"):
            return 15
        elif (s == "P"):
            return 16
        elif (s == "Q"):
            return 17
        elif (s == "R"):
            return 18
        elif (s == "S"):
            return 19
        elif (s == "T"):
            return 20
        elif (s == "U"):
            return 21
        elif (s == "V"):
            return 22
        elif (s == "W"):
            return 23
        elif (s == "X"):
            return 24
        elif (s == "Y"):
            return 25
        elif (s == "Z"):
            return 26

    def titleToNumberNew(self, s: str) -> int:
        x = 0
        for i in s:
            x = x * 26 + (ord(i) - 64)

        return (x)


sol = Solution()
st = ""
print(sol.titleToNumer(st))