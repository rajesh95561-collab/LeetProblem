class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        target_idx = 0
        result = []
        for num in range(1,target[-1]+1):
            result.append("Push")
            if num == target[target_idx]:
                target_idx+=1
            else:
              result.append("Pop")
        return result  