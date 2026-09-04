class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        temp = nums[0]
        maxi = []
        for i in nums:
            temp = max(temp,i)
            maxi.append(temp)
        temp = nums[-1]
        mini = []
        for i in range(len(nums)-1,-1,-1):
            temp = min(temp,nums[i])
            mini.append(temp)
        mini[:] = mini[::-1]
        print(maxi)
        print(mini)
        for i in range(len(nums)):
            if maxi[i]-mini[i] <= k:
                return i
        return -1