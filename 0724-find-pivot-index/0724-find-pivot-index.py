class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        if len(nums)==1:
            return 0
        n = len(nums)
        prefix = []
        add = 0
        left = -1
        for i in nums:
            prefix.append(add)
            add+=i
        add = 0
        for i in range(n-1,-1,-1):
            if prefix[i] == add:
                left = i
            add+=nums[i]
        return left