class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        a=0
        for i in nums:
           a|=i
        return a*(1<<(len(nums)-1))