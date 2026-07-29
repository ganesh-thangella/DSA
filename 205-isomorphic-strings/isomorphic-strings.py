class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_st = {}
        map_ts = {}

        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]

            if c1 not in map_st and c2 not in map_ts:
                map_st[c1] = c2
                map_ts[c2] = c1
            elif map_st.get(c1) != c2 or map_ts.get(c2) != c1:
                return False

        return True