class Solution:
    def countCommas(self, n: int) -> int:
        l = 1000
        commas = 0
        while l <= n :
            commas += n-l+1
            l*=1000
        return commas