class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = 0
        max_avg = float("-inf")
        j = k*(-1) + 1
        for i in range(len(nums)):
            curr_sum += nums[i]
            if j > 0:
                curr_sum -= nums[j - 1]
            if(j >= 0):
                max_avg = max(max_avg,curr_sum/k)
            j+=1
        return max_avg
