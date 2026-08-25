class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        myset=set(sentence)
        return len(myset)==26