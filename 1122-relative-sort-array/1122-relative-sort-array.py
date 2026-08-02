class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        dict_map = {}
        for i in arr2:
            dict_map[i] = dict_map.get(i,0)
        arr1.sort()
        for i in arr1:
            dict_map[i] = dict_map.get(i,0)+1
        for idx,freq in dict_map.items():
            for _ in range(freq):
                result.append(idx)
        return result