# https://leetcode.com/problems/goal-parser-interpretation/

class Solution:
    def interpret(self, command: str) -> str:
        mystr = ""
        i = 0
        while i < len(command):
            if command[i] == "G":
                mystr = mystr + "G"
                i += 1
            elif command[i] == "(" and command[i+1] == ")":
                mystr = mystr + "o"
                i += 2
            else:
                mystr = mystr + "al"
                i += 4

        return mystr


sol = Solution()

mycommand = "G()(al)"
print(sol.interpret(mycommand))

mycommand = "G()()()()(al)"
print(sol.interpret(mycommand))

mycommand = "(al)G(al)()()G"
print(sol.interpret(mycommand))