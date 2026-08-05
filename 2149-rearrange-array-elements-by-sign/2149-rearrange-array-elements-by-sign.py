class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)
        i = 0
        j=i+1
        for _ in nums:
            if _ > 0:
                result[i]=_
                i+=2
            else:
                result[j]=_
                j+=2
        return result