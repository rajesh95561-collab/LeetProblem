class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        my = {}
        for i in nums:
            if i%2 == 0:
                my[i] = my.get(i,0)+1 
        maxi = float("-inf")
        maxi_freq = float("-inf")
        for item,freq in my.items():
            if maxi_freq == freq:
                maxi = min(maxi,item)
            elif maxi_freq < freq:
                maxi = item
                maxi_freq = freq
        return maxi if maxi != float("-inf") else -1