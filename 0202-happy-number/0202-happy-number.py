class Solution:
    def isHappy(self, n: int) -> bool:
        sol_list=[]
        while True:
            total = 0
            while n >=1 :
                x = n%10
                total += (x*x)
                n//=10
            if total == 1:
                return True
            elif total in sol_list:
                return False
            else:
                sol_list.append(total)
                n = total
