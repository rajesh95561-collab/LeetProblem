class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(pow(c,1/2))
        while i<=j:
            if pow(i,2)+pow(j,2) == c:
                return True
            elif pow(i,2)+pow(j,2) < c:
                i+=1
            else:
                j-=1
        return False