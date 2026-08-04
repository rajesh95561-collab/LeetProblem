class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        max_c = float("-inf")
        for i in range(len(nums)):
            total+=nums[i]
            max_c = max(total,max_c)
            if total < 0:
                total = 0
        return max_c