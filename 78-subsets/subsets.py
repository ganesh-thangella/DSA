class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        a=[[]]
        for i in nums:
            a+=[cur+[i] for cur in a]
        return a