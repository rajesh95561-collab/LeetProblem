class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*n
        stack = []
        for i in range(n-1,-1,-1):
            while stack and stack[-1][1] <= temperatures[i]:
                stack.pop()
            if len(stack) != 0:
                result[i] = abs(stack[-1][0] - i)
            stack.append([i,temperatures[i]])
        return result