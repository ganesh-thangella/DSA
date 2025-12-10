class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=sorted(strs)
        f=s[0]
        l=s[-1]
        a=""
        for i in range(len(f)):
            if f[i]!=l[i]:
                return a
            a+=f[i]
        return a