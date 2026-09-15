class Solution:
    def backtrack(self,idx,temp,result,digits,my_dict):
        if idx == len(digits):
            result.append("".join(temp))
            return
        for i in my_dict[digits[idx]]:
            temp.append(i)
            self.backtrack(idx+1,temp,result,digits,my_dict)
            temp.pop()
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        my_dict = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        result = []
        self.backtrack(0,[],result,digits,my_dict)
        return result