class Solution:
    def minOperations(self, s: str) -> int:
        a,b=0,0
        n=len(s)
        for i in s:
            if int(i)==b:
                a+=1
            b^=1
        return min(a,n-a)