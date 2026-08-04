class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        result = []
        j=0
        nums.sort()
        for i in range(nums[0],nums[-1]):
            if nums[j] != i:
                result.append(i)
            else:
                j+=1
        return result