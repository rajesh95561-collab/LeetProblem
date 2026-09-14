class Solution:
    def backtrack(self,idx,k,n,sub,result):
        if k == 0 and n == 0:
            result.append(sub.copy())
            return
        if k < 0 or n < 0: return 
        if idx == 10: return
        for i in range(idx,10):
            sub.append(i)
            self.backtrack(i+1,k-1,n-i,sub,result)
            sub.pop()
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        self.backtrack(1,k,n,[],result)
        return result