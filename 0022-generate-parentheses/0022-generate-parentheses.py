class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(ob,cb,s):
            if ob == n and cb == n:
                result.append(s)
                return
            if ob < n:
                backtrack(ob+1,cb,s+"(")
            if cb < ob:
                backtrack(ob,cb+1,s+")")
        backtrack(0,0,"")
        return result