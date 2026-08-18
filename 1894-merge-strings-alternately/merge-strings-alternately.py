class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = ""
        min_len = min(len(word1), len(word2))

        for i in range(min_len):
            result += word1[i] + word2[i]

        if len(word1) > len(word2):
            result += word1[min_len:]
        else:
            result += word2[min_len:]
            
        return result