class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        f=Counter(nums)
        nums.sort(key=lambda x:(f[x],-x))
        return nums