class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a=set(allowed)
        count=0
        for i in words:
            consistant=True
            for ch in i:
                if ch not in a:
                    consistant=False
                    break
            if consistant:
                count+=1
        return count