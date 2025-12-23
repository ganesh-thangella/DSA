class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a=True
        for i in ransomNote:
            if ransomNote.count(i)>magazine.count(i):
                a=False
        return a