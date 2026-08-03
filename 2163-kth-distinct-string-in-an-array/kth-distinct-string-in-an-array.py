class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d={}
        count=0
        for i in arr:
            if i in d:
                d[i]=False
            else:
                d[i]=True
        for i in arr:
            if d[i]:
                count+=1
            if count==k:
                return i
        return ""