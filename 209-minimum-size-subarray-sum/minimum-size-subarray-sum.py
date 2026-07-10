class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans=float("inf")
        cur_sum=0
        l=0
        for i in range(len(nums)):
            cur_sum+=nums[i]
            while cur_sum>=target:
                ans=min(ans,i-l+1)
                cur_sum-=nums[l]
                l+=1
        return 0 if ans==float("inf")  else    ans