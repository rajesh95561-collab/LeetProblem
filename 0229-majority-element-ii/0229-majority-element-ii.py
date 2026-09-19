class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        #Moore's  voting algo
        n = len(nums)
        el1 = None
        el2 = None
        count1 = 0
        count2 = 0
        result = []
        occ = n//3
        # find the 2 element which has more frequency
        for i in nums:
            if count1 == 0 and i != el2:
                count1+=1
                el1 = i
            elif count2 == 0 and i != el1:
                count2+=1
                el2 = i
            elif el1 == i:
                count1+=1
            elif el2 == i:
                count2+=1
            else:
                count1-=1
                count2-=1
        # find the selected element frequency
        count1 = 0
        count2 = 0
        for i in nums:
            if i == el1: count1+=1
            elif i == el2: count2+=1
        #check the given condition
        if count1 > occ:result.append(el1)
        if count2 > occ:result.append(el2)
        #return the result in sorted order
        return sorted(result)