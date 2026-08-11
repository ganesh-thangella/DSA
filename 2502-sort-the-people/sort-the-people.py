class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        a=dict(zip(heights,names))
        s=sorted(heights,reverse=True)
        res=[a[i] for i in s]
        return res