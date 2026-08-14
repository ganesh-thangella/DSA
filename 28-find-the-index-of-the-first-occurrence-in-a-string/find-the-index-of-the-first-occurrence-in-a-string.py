class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a=len(needle)
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+a]==needle:
                return i
        else:
            return -1