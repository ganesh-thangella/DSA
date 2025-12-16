class Solution:
    def maxDifference(self, s: str) -> int:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        n=len(s)
        e=0
        for i in d:
            if d[i]%2==0:
                if d[i]<n:
                    n=d[i]
            else:
                if d[i]>e:
                    e=d[i]
        if n==len(s):
            n=0
        return e-n