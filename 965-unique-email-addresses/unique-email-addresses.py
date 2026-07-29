class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res=set()
        for i in emails:
            local,domain=i.split('@')
            temp=""
            for j in local:
                if j=="+":
                    break
                elif j==".":
                    continue
                else:
                    temp+=j
            res.add(temp+"@"+domain)
        return len(res)