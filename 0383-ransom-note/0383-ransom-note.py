class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_ransomNote = {}
        dict_magazine = {}
        for i in ransomNote:
            dict_ransomNote[i] = dict_ransomNote.get(i,0)+1
        for i in magazine:
            dict_magazine[i] = dict_magazine.get(i,0)+1
        for ch,count in dict_ransomNote.items():
            if dict_magazine.get(ch,0)<count:
                return False
        return True