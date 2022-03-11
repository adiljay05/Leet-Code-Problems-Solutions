class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        strings = sentence.split(' ')
        for i in range(len(strings)):
            found = True
            for j in range(len(searchWord)):
                if strings[i][j]!=searchWord[j] or len(strings[i])<len(searchWord):
                    found = False
                    break
            if found:
                return i+1
        return -1