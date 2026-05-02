class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l=0
        n=len(s)
        d={}
        ans=0
        for r in range(n):
            if s[r] in d:
                d[s[r]]+=1
            else:
                d[s[r]]=1
            if r-l==3:
                d[s[l]]-=1
                if d[s[l]]==0:
                    d.pop(s[l])
                l+=1
            if len(d)==3:
                ans+=1
        return ans