#Solve using memorization
class Solution:
    def track(self,n,dp):
        if n == 0: return 0
        if n == 1: return 1
        if dp[n] != -1: return dp[n]
        dp[n] = self.track(n-1,dp) + self.track(n-2,dp)
        return dp[n]
    def fib(self, n: int) -> int:
        dp = [-1] * (n+1)
        return self.track(n,dp)
        