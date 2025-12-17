class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l,r=0,sum(nums)
        for i,j in enumerate(nums):
            r-=j
            if l==r:
                return i
            l+=j
        return -1