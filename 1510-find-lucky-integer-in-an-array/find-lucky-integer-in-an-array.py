class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d={}
        m=-1
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i,j in d.items():
            if i==j:
                m=max(m,i)

        return m