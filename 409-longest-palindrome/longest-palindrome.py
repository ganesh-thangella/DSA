class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        c=0
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
            if d[i]%2==1:
                c+=1
            else: c-=1
        if c>1:
            return len(s)-c+1
        return len(s)