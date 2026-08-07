class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n=len(words)
        d={}
        for i in words:
            for j in i:
                if j in d:
                    d[j]+=1
                else:
                    d[j]=1
        for a in d.values():
            if a%n!=0:
                return False
        return True