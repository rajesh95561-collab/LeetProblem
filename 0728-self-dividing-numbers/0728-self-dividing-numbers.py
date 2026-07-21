class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        sol=[]
        def solution(num):
            temp = num
            while(temp > 0):
                digit = temp % 10
                if digit == 0 or num % digit != 0:
                    return False
                temp //= 10
            return True
        for x in range(left,right+1):
            if solution(x):
                sol.append(x)
        return sol