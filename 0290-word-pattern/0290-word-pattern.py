class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict_s = {}
        dict_pattern = {}
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        for c1,c2 in zip(pattern,s):
            if c1 in dict_s:
                if dict_s[c1] != c2:
                    return False
            else:
                dict_s[c1] = c2
            if c2 in dict_pattern:
                if dict_pattern[c2] != c1:
                    return False
            else:
                dict_pattern[c2] = c1
        return True