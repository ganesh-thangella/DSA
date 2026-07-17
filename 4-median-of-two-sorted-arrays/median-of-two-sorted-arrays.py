class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a=nums1+nums2
        b=sorted(a)
        mid=len(b)//2
        if len(b)%2!=0:
            return b[mid]
        else:
            return (b[mid]+b[mid-1])/2