class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans=0
        a=set(s)
        for i in a:
            l=s.find(i)
            r=s.rfind(i)
            if l<r:
                ans+=len(set(s[l+1:r]))
        return ans