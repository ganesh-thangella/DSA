class Solution:
    def customSortString(self, order: str, s: str) -> str:
        c=Counter(s)
        a=[]
        for i in order:
            if i in c:
                a.append(i*c[i])
                del c[i]
        for i,count in c.items():
            a.append(i*count)
        return "".join(a)