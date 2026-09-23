class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        my_dict = {0:1}
        count = 0
        current_sum = 0
        for i in nums:
            current_sum+=i
            need = current_sum - k
            if need in my_dict:
                count+=my_dict[need]
            my_dict[current_sum] = my_dict.get(current_sum,0)+1
        return count