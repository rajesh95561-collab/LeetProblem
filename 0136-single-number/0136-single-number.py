class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        val = 0
        for i in nums:
            val ^= i
        return val