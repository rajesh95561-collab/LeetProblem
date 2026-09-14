class Solution:
    def backtrack(self,idx,total,sub,candidates,result):
        if total == 0:
            result.append(sub.copy())
            return
        if total < 0: return 
        if idx == len(candidates): return
        for i in range(idx,len(candidates)):
            if idx < i and candidates[i] == candidates[i-1]:
                continue
            sub.append(candidates[i])
            self.backtrack(i+1,total-candidates[i],sub,candidates,result)
            sub.pop()
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        self.backtrack(0,target,[],candidates,result)
        return result
        