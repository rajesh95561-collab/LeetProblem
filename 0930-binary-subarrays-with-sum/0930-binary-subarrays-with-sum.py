class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        mapp = {0:1}
        count = 0
        cs = 0
        for i in nums:
            cs+=i
            need = cs - goal
            if need in mapp:
                count += mapp[need]
            mapp[cs] = mapp.get(cs,0)+1
        return count