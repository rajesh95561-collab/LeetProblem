class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        for c1,c2 in zip(s,t):
            if c1 in dict_s:
                if dict_s[c1] != c2:
                    return False
            else:
                dict_s[c1] = c2
            if c2 in dict_t:
                if dict_t[c2] != c1:
                    return False
            else:
                dict_t[c2] = c1
        return True

        
        