class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)//2
        first_half = "".join(sorted(s[:n]))
        print(first_half)
        second_half = "".join(reversed(first_half))
        print(second_half)
        if len(s)%2 == 0:
            return first_half + second_half
        else:
            return first_half + s[n] + second_half
