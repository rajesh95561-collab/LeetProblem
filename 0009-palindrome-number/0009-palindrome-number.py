class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        total = 0
        while num > 0:
            digit = num%10
            total = (total*10) + digit
            num//=10
        return x == total

