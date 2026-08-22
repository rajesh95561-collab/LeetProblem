class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        result = []
        for i in range(1,n+1):
            if i > target[-1]:
                break
            stack.append(i)
            result.append("Push")
            if stack[-1] not in target:
                stack.pop()
                result.append("Pop")
        return result    