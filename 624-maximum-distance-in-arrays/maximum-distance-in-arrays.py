class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        m=arrays[0][0]
        n=arrays[0][-1]
        max_dist=0
        for i in range(1,len(arrays)):
            max_dist=max(max_dist,abs(arrays[i][-1]-m),abs(n-arrays[i][0]))
            m=min(m,arrays[i][0])
            n=max(n,arrays[i][-1])
        return max_dist