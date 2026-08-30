class Solution:
    def countDigits(self, num: int) -> int:
        c=0
        s=str(num)
        for i in range(len(s)):
            if num%(int(s[i]))==0:
                c+=1
        return c