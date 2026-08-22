class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_product = 1
        x = str(n)
        for i in range(len(x)-1,-1,-1):
            digit_sum += int(x[i])
            digit_product *= int(x[i])
        return n % (digit_sum + digit_product) == 0
        