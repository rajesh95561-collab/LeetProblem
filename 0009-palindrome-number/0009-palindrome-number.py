class Solution:
    def isPalindrome(self, x: int) -> bool:
        X = list(str(x))
        return X == X[::-1]

        