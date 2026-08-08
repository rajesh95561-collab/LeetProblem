class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        sol = start ^ goal
        count = 0
        for i in range(0,32):
            if (sol & (1<<i)) != 0:
                count+=1
        return count