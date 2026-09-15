class Solution:
    def backtrack(self,idx,temp,result,digits,my_dict):
        if idx == len(digits):
            result.append(temp)
            return
        for i in my_dict[digits[idx]]:
            temp+=i
            self.backtrack(idx+1,temp,result,digits,my_dict)
            temp = temp[:-1]
    def letterCombinations(self, digits: str) -> List[str]:
        my_dict = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        result = []
        self.backtrack(0,"",result,digits,my_dict)
        return result