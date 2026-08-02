class Solution:
    def merge(self,left,right):
        result = []
        i,j=0,0
        m,n=len(left),len(right)
        while i<m and j<n:
            if left[i]<=right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        while i<m:
            result.append(left[i])
            i+=1
        while j<n:
            result.append(right[j])
            j+=1
        return result
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        mid  = len(nums)//2
        left_arr = nums[:mid]
        right_arr = nums[mid:]
        left = self.sortArray(left_arr)
        right = self.sortArray(right_arr)
        return self.merge(left,right)