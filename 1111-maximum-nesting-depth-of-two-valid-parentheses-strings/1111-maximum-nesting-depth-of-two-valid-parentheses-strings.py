class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        result = []
        depth = 0
        for i in seq:
            if i == "(":
                depth+=1
            if depth % 2 == 0: result.append(1)
            else: result.append(0)
            if i == ")":
                depth-=1
        return result
