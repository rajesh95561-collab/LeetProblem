class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = []
        m = len(nums1)
        n = len(nums2)
        i,j = 0,0 
        while i < m and j < n:
            if nums1[i] > nums2[j]:
                result.append(nums2[j])
                j+=1
            else:
                result.append(nums1[i])
                i+=1
        while i < m:
            result.append(nums1[i])
            i+=1
        while j < n:
            result.append(nums2[j])
            j+=1
        k = len(result)
        n = k//2
        if k%2 == 0:
            return float((result[n-1]+result[n])/2)
        else:
            return float(result[n])
