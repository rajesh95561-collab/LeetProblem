class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if nums[0] == target:
            return 1
        j = 0
        length = float("inf")
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            while curr_sum >= target:
                l = i-j+1
                length = min(length,l)
                curr_sum -= nums[j]
                j+=1
        if length == float("inf"):return 0
        else:return length