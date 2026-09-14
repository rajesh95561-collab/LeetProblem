class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        n = len(nums)
        for i in range(0,2**n):
            lst = tuple()
            for j in range(n):
                if (i & (1<<j)) != 0:
                    lst+=(nums[j],)
            result.add(lst)
        return list(result)