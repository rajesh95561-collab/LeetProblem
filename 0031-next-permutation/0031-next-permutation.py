class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        idx1 = -1
        idx2 = -1
        #find the smallest number index from the right side
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                idx1 = i
                break
        #if there is no element return the nums in rreverse order
        if idx1 == -1:
            nums[:] = nums[::-1]
            return nums
        #then find the next greater element then the nums[idx1] 
        for i in range(idx1+1,n):
            if nums[idx1] < nums[i]:
                idx2 = i
        #then swap the 2 element
        nums[idx1],nums[idx2] = nums[idx2],nums[idx1]
        #swap the suffix after the index1 inplace
        i = idx1+1
        j = n-1
        while i < j:
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
            j-=1