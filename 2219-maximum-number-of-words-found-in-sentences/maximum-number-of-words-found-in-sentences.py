class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        m=0
        for i in sentences:
            c=i.count(" ")+1
            if c>m:
                m=c
            else:
                m=m
        return m