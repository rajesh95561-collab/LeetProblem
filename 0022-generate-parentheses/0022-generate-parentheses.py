class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        sub = [""]*(n*2)
        def backtrack(idx,total,sub):
            if idx == len(sub):
                if total == 0:
                    result.append("".join(sub))
                return
            if total < 0:return
            if total > len(sub)//2:return
            
            sub[idx]="("
            sumi = total+1
            backtrack(idx+1,sumi,sub)
            sub[idx]=")"
            sumi = total-1
            backtrack(idx+1,sumi,sub)
        backtrack(0,0,sub)
        return result