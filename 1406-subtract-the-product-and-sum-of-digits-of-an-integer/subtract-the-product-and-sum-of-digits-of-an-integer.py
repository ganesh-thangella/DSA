class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p=1
        s=0
        while n>0:
            temp=n%10
            p*=temp
            s+=temp
            n//=10
        return p-s
