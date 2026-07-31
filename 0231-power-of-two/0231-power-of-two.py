class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        temp = n
        while temp >=1:
            if temp == 1:
                return True
            temp = temp/2
        return False