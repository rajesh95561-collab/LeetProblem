class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_t = {'(':')','{':'}','[':']'}
        for i in s:
            if i in dict_t:
                stack.append(i)
            else:
                if not stack:
                    return False
                if dict_t[stack.pop()] != i:
                    return False
        return not stack