class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0        
        my_set = set(nums)
        max_length = 1
        for num in my_set: 
            if num-1 not in my_set:
                i=1
                while num+i in my_set:
                    i+=1
                max_length=max(i,max_length)
        
        return max_length