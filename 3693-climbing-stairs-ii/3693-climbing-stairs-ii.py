class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        if n == 0: return 0
        pre1, pre2, pre3 = 0, float("inf"), float("inf")
        for i in range(1,n+1):
            jump1 = pre1 + costs[i-1] + 1
            if i > 1:
                jump2 = pre2 + costs[i-1] + 4
            else: jump2 = float("inf")
            if i > 2:
                jump3 = pre3 + costs[i-1] + 9
            else: jump3 = float("inf")
            curr = min(jump1, jump2, jump3)
            pre3, pre2, pre1= pre2, pre1, curr
        return pre1