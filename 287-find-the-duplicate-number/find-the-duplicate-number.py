class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        k = len(nums) - len(set(nums)) + 1
        return (sum(nums) - sum(set(nums))) // (k - 1)