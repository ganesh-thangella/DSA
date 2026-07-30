class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sum=0
        for i in words:
            flag=True
            temp=chars
            for j in i:
                if j in temp:
                    temp=temp.replace(j,"",1)
                else:
                    flag=False
                    break
            if flag:
                sum+=len(i)
        return sum
