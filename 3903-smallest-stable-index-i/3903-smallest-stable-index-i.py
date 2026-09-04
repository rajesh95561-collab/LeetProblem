class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        maxi = [nums[0]]*n
        mini = [nums[-1]]*n
        for i in range(1,n):
            maxi[i] = max(nums[i],maxi[i-1])
            mini[n-1-i] = min(mini[n-i],nums[n-1-i])
        for i in range(len(nums)):
            if maxi[i]-mini[i] <= k:
                return i
        return -1