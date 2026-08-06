class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        temp = n
        digit_mul = 1
        while temp > 0:
            digit_mul *= temp%10
            temp//=10
        if digit_mul%t == 0:
            return n
        else:
            return self.smallestNumber(n+1,t)
