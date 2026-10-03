class Solution:
    def longestValidParentheses(self, s: str) -> int:
        o = 0
        c = 0
        resultL = 0
        for i in s:
            if i == "(": o+=1
            else: c+=1
            if o == c:
                resultL = max(resultL,o+c)
            if c > o:
                o, c = 0, 0
        o = 0
        c = 0
        resultR = 0
        n = len(s)
        for i in range(n-1,-1,-1):
            if s[i] == "(": o+=1
            else: c+=1
            if o == c:
                resultR = max(resultR,o+c)
            if o > c:
                o, c = 0, 0
        return max(resultL,resultR)