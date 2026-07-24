class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict_s = {}
        for i in s:
            dict_s[i]= dict_s.get(i,0)+1
        for ch,count in dict_s.items():
            if count == 1:
                return s.index(ch)
        return -1
        