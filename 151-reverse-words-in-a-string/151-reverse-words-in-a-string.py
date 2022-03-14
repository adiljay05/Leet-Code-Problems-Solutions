class Solution:
    def reverseWords(self, s: str) -> str:
        # print(s.strip().split(' ')[::-1])
        return " ".join(re.sub(' +', ' ',s).strip().split(' ')[::-1])