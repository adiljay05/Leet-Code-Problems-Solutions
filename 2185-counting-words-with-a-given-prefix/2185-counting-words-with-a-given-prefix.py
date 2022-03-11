class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # count = 0
        # for i in range(len(words)):
        #     found = True
        #     for j in range(len(pref)):
        #         if words[i][j]!=pref[j] or len(words[i])<len(pref):
        #             found = False
        #             break
        #     if found:
        #         count+=1
        # return count
        count = 0
        lenPref = len(pref)
        for word in words:
            if pref == word[0:lenPref]:
                count+=1
        return count